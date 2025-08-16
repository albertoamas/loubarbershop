/**
 * ExportService - Servicio para exportación de datos en diferentes formatos
 */
class ExportService {
  
  /**
   * Exportar datos a CSV
   */
  static exportToCSV(data, filename = 'export') {
    try {
      if (!Array.isArray(data) || data.length === 0) {
        throw new Error('Los datos deben ser un array no vacío')
      }

      // Obtener headers del primer objeto
      const headers = Object.keys(data[0])
      
      // Crear contenido CSV
      let csvContent = headers.join(',') + '\n'
      
      data.forEach(row => {
        const values = headers.map(header => {
          let value = row[header] || ''
          // Escapar comillas y envolver en comillas si contiene comas
          if (typeof value === 'string' && (value.includes(',') || value.includes('"'))) {
            value = '"' + value.replace(/"/g, '""') + '"'
          }
          return value
        })
        csvContent += values.join(',') + '\n'
      })

      // Crear y descargar archivo
      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' })
      const link = document.createElement('a')
      
      if (link.download !== undefined) {
        const url = URL.createObjectURL(blob)
        link.setAttribute('href', url)
        link.setAttribute('download', `${filename}-${this.getDateString()}.csv`)
        link.style.visibility = 'hidden'
        document.body.appendChild(link)
        link.click()
        document.body.removeChild(link)
        URL.revokeObjectURL(url)
      }
      
      return { success: true, message: 'Archivo CSV descargado exitosamente' }
    } catch (error) {
      console.error('Error al exportar CSV:', error)
      throw new Error('No se pudo exportar el archivo CSV')
    }
  }

  /**
   * Exportar datos a JSON
   */
  static exportToJSON(data, filename = 'export') {
    try {
      const jsonContent = JSON.stringify(data, null, 2)
      const blob = new Blob([jsonContent], { type: 'application/json' })
      
      const link = document.createElement('a')
      const url = URL.createObjectURL(blob)
      link.setAttribute('href', url)
      link.setAttribute('download', `${filename}-${this.getDateString()}.json`)
      link.style.visibility = 'hidden'
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      URL.revokeObjectURL(url)
      
      return { success: true, message: 'Archivo JSON descargado exitosamente' }
    } catch (error) {
      console.error('Error al exportar JSON:', error)
      throw new Error('No se pudo exportar el archivo JSON')
    }
  }

  /**
   * Exportar tabla HTML a Excel (simulado con HTML)
   */
  static exportTableToExcel(tableData, filename = 'export') {
    try {
      if (!Array.isArray(tableData) || tableData.length === 0) {
        throw new Error('Los datos de la tabla deben ser un array no vacío')
      }

      const headers = Object.keys(tableData[0])
      
      // Crear tabla HTML
      let htmlContent = '<table border="1">'
      
      // Headers
      htmlContent += '<thead><tr>'
      headers.forEach(header => {
        htmlContent += `<th>${this.escapeHtml(header)}</th>`
      })
      htmlContent += '</tr></thead>'
      
      // Body
      htmlContent += '<tbody>'
      tableData.forEach(row => {
        htmlContent += '<tr>'
        headers.forEach(header => {
          const value = row[header] || ''
          htmlContent += `<td>${this.escapeHtml(String(value))}</td>`
        })
        htmlContent += '</tr>'
      })
      htmlContent += '</tbody></table>'

      // Crear blob con formato Excel
      const blob = new Blob([htmlContent], { 
        type: 'application/vnd.ms-excel' 
      })
      
      const link = document.createElement('a')
      const url = URL.createObjectURL(blob)
      link.setAttribute('href', url)
      link.setAttribute('download', `${filename}-${this.getDateString()}.xls`)
      link.style.visibility = 'hidden'
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      URL.revokeObjectURL(url)
      
      return { success: true, message: 'Archivo Excel descargado exitosamente' }
    } catch (error) {
      console.error('Error al exportar Excel:', error)
      throw new Error('No se pudo exportar el archivo Excel')
    }
  }

  /**
   * Exportar gráfico como imagen
   */
  static exportChartAsImage(chartInstance, filename = 'chart') {
    try {
      if (!chartInstance) {
        throw new Error('Instancia de gráfico no válida')
      }

      const canvas = chartInstance.canvas
      const url = canvas.toDataURL('image/png', 1.0)
      
      const link = document.createElement('a')
      link.download = `${filename}-${this.getDateString()}.png`
      link.href = url
      link.click()
      
      return { success: true, message: 'Gráfico descargado exitosamente' }
    } catch (error) {
      console.error('Error al exportar gráfico:', error)
      throw new Error('No se pudo exportar el gráfico')
    }
  }

  /**
   * Generar reporte PDF (simulado con HTML para impresión)
   */
  static generatePDFReport(reportData, title = 'Reporte') {
    try {
      const printWindow = window.open('', '_blank')
      
      const htmlContent = `
        <!DOCTYPE html>
        <html>
        <head>
          <title>${title}</title>
          <style>
            body {
              font-family: Arial, sans-serif;
              margin: 40px;
              color: #333;
            }
            h1 {
              color: #2563eb;
              border-bottom: 2px solid #e5e7eb;
              padding-bottom: 10px;
            }
            h2 {
              color: #374151;
              margin-top: 30px;
            }
            table {
              width: 100%;
              border-collapse: collapse;
              margin: 20px 0;
            }
            th, td {
              border: 1px solid #d1d5db;
              padding: 12px;
              text-align: left;
            }
            th {
              background-color: #f3f4f6;
              font-weight: bold;
            }
            .header {
              text-align: center;
              margin-bottom: 30px;
            }
            .date {
              text-align: right;
              font-size: 12px;
              color: #6b7280;
            }
            .section {
              margin: 30px 0;
            }
            @media print {
              body { margin: 20px; }
              .no-print { display: none; }
            }
          </style>
        </head>
        <body>
          <div class="header">
            <h1>${title}</h1>
            <div class="date">Generado el: ${new Date().toLocaleDateString()}</div>
          </div>
          
          ${this.generateReportHTML(reportData)}
          
          <div class="no-print" style="text-align: center; margin-top: 30px;">
            <button onclick="window.print()" style="padding: 10px 20px; background: #2563eb; color: white; border: none; border-radius: 5px; cursor: pointer;">
              Imprimir / Guardar como PDF
            </button>
            <button onclick="window.close()" style="padding: 10px 20px; background: #6b7280; color: white; border: none; border-radius: 5px; cursor: pointer; margin-left: 10px;">
              Cerrar
            </button>
          </div>
        </body>
        </html>
      `
      
      printWindow.document.write(htmlContent)
      printWindow.document.close()
      
      return { success: true, message: 'Reporte PDF generado exitosamente' }
    } catch (error) {
      console.error('Error al generar PDF:', error)
      throw new Error('No se pudo generar el reporte PDF')
    }
  }

  /**
   * Generar HTML para diferentes tipos de reportes
   */
  static generateReportHTML(reportData) {
    if (!reportData) return '<p>No hay datos para mostrar</p>'

    let html = ''

    // Si es un array de objetos (tabla)
    if (Array.isArray(reportData)) {
      if (reportData.length > 0) {
        const headers = Object.keys(reportData[0])
        html += '<div class="section"><table>'
        
        // Headers
        html += '<thead><tr>'
        headers.forEach(header => {
          html += `<th>${this.escapeHtml(this.formatHeader(header))}</th>`
        })
        html += '</tr></thead>'
        
        // Rows
        html += '<tbody>'
        reportData.forEach(row => {
          html += '<tr>'
          headers.forEach(header => {
            const value = row[header] || ''
            html += `<td>${this.escapeHtml(String(value))}</td>`
          })
          html += '</tr>'
        })
        html += '</tbody></table></div>'
      }
    }
    // Si es un objeto con secciones
    else if (typeof reportData === 'object') {
      Object.keys(reportData).forEach(section => {
        html += `<div class="section"><h2>${this.formatHeader(section)}</h2>`
        
        const sectionData = reportData[section]
        if (Array.isArray(sectionData)) {
          html += this.generateReportHTML(sectionData)
        } else if (typeof sectionData === 'object') {
          html += '<ul>'
          Object.keys(sectionData).forEach(key => {
            html += `<li><strong>${this.formatHeader(key)}:</strong> ${sectionData[key]}</li>`
          })
          html += '</ul>'
        } else {
          html += `<p>${sectionData}</p>`
        }
        
        html += '</div>'
      })
    }

    return html
  }

  /**
   * Escapar HTML para prevenir XSS
   */
  static escapeHtml(text) {
    const div = document.createElement('div')
    div.textContent = text
    return div.innerHTML
  }

  /**
   * Formatear headers para mostrar
   */
  static formatHeader(header) {
    return header
      .replace(/([A-Z])/g, ' $1')
      .replace(/^./, str => str.toUpperCase())
      .trim()
  }

  /**
   * Obtener string de fecha para nombres de archivo
   */
  static getDateString() {
    const now = new Date()
    const year = now.getFullYear()
    const month = String(now.getMonth() + 1).padStart(2, '0')
    const day = String(now.getDate()).padStart(2, '0')
    const hours = String(now.getHours()).padStart(2, '0')
    const minutes = String(now.getMinutes()).padStart(2, '0')
    
    return `${year}${month}${day}-${hours}${minutes}`
  }

  /**
   * Validar formato de exportación
   */
  static validateExportFormat(format) {
    const validFormats = ['csv', 'json', 'excel', 'pdf', 'png']
    return validFormats.includes(format.toLowerCase())
  }

  /**
   * Obtener tipo MIME por formato
   */
  static getMimeType(format) {
    const mimeTypes = {
      csv: 'text/csv',
      json: 'application/json',
      excel: 'application/vnd.ms-excel',
      pdf: 'application/pdf',
      png: 'image/png'
    }
    return mimeTypes[format.toLowerCase()] || 'application/octet-stream'
  }
}

export default ExportService
