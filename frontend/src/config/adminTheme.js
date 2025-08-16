// config/adminTheme.js - Configuración del tema administrativo
export const adminTheme = {
  // Colores principales del panel administrativo
  colors: {
    // Colores primarios
    primary: {
      50: '#eff6ff',
      100: '#dbeafe',
      200: '#bfdbfe',
      300: '#93c5fd',
      400: '#60a5fa',
      500: '#3b82f6', // Color principal
      600: '#2563eb',
      700: '#1d4ed8',
      800: '#1e40af',
      900: '#1e3a8a'
    },
    
    // Colores de estado
    success: {
      50: '#f0fdf4',
      500: '#22c55e',
      600: '#16a34a',
      700: '#15803d'
    },
    warning: {
      50: '#fffbeb',
      500: '#f59e0b',
      600: '#d97706',
      700: '#b45309'
    },
    danger: {
      50: '#fef2f2',
      500: '#ef4444',
      600: '#dc2626',
      700: '#b91c1c'
    },
    info: {
      50: '#f0f9ff',
      500: '#06b6d4',
      600: '#0891b2',
      700: '#0e7490'
    },
    
    // Colores neutros
    gray: {
      50: '#f9fafb',
      100: '#f3f4f6',
      200: '#e5e7eb',
      300: '#d1d5db',
      400: '#9ca3af',
      500: '#6b7280',
      600: '#4b5563',
      700: '#374151',
      800: '#1f2937',
      900: '#111827'
    }
  },
  
  // Tipografía
  typography: {
    fontFamily: {
      sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
      mono: ['JetBrains Mono', 'Monaco', 'Consolas', 'Liberation Mono', 'Courier New', 'monospace']
    },
    fontSize: {
      xs: ['0.75rem', { lineHeight: '1rem' }],
      sm: ['0.875rem', { lineHeight: '1.25rem' }],
      base: ['1rem', { lineHeight: '1.5rem' }],
      lg: ['1.125rem', { lineHeight: '1.75rem' }],
      xl: ['1.25rem', { lineHeight: '1.75rem' }],
      '2xl': ['1.5rem', { lineHeight: '2rem' }],
      '3xl': ['1.875rem', { lineHeight: '2.25rem' }]
    }
  },
  
  // Espaciado
  spacing: {
    xs: '0.5rem',    // 8px
    sm: '0.75rem',   // 12px
    md: '1rem',      // 16px
    lg: '1.5rem',    // 24px
    xl: '2rem',      // 32px
    '2xl': '3rem',   // 48px
    '3xl': '4rem'    // 64px
  },
  
  // Bordes redondeados
  borderRadius: {
    none: '0',
    sm: '0.125rem',
    md: '0.375rem',
    lg: '0.5rem',
    xl: '0.75rem',
    full: '9999px'
  },
  
  // Sombras
  boxShadow: {
    sm: '0 1px 2px 0 rgb(0 0 0 / 0.05)',
    md: '0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)',
    lg: '0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)',
    xl: '0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)'
  },
  
  // Configuración del sidebar
  sidebar: {
    width: {
      collapsed: '4rem',    // 64px
      expanded: '16rem'     // 256px
    },
    backgroundColor: '#1f2937',  // gray-800
    textColor: '#e5e7eb',        // gray-200
    hoverColor: '#374151',       // gray-700
    activeColor: '#3b82f6'       // blue-500
  },
  
  // Configuración del header
  header: {
    height: '4rem',              // 64px
    backgroundColor: '#ffffff',  // white
    borderColor: '#e5e7eb',      // gray-200
    textColor: '#1f2937'         // gray-800
  },
  
  // Configuración de formularios
  forms: {
    input: {
      borderColor: '#d1d5db',      // gray-300
      focusBorderColor: '#3b82f6', // blue-500
      backgroundColor: '#ffffff',  // white
      textColor: '#1f2937'         // gray-800
    },
    button: {
      primary: {
        backgroundColor: '#3b82f6', // blue-500
        hoverColor: '#2563eb',      // blue-600
        textColor: '#ffffff'        // white
      },
      secondary: {
        backgroundColor: '#6b7280', // gray-500
        hoverColor: '#4b5563',      // gray-600
        textColor: '#ffffff'        // white
      }
    }
  },
  
  // Configuración de tablas
  table: {
    headerBackground: '#f9fafb',  // gray-50
    borderColor: '#e5e7eb',       // gray-200
    hoverColor: '#f9fafb',        // gray-50
    stripedColor: '#f9fafb'       // gray-50
  },
  
  // Configuración de cards
  card: {
    backgroundColor: '#ffffff',   // white
    borderColor: '#e5e7eb',       // gray-200
    shadowColor: 'rgb(0 0 0 / 0.1)'
  },
  
  // Configuración de modales
  modal: {
    overlayColor: 'rgb(0 0 0 / 0.5)',
    backgroundColor: '#ffffff',   // white
    borderColor: '#e5e7eb'        // gray-200
  },
  
  // Breakpoints responsive
  breakpoints: {
    sm: '640px',
    md: '768px',
    lg: '1024px',
    xl: '1280px',
    '2xl': '1536px'
  },
  
  // Transiciones
  transitions: {
    fast: '150ms',
    normal: '300ms',
    slow: '500ms'
  },
  
  // Z-index scale
  zIndex: {
    dropdown: 1000,
    sticky: 1020,
    fixed: 1030,
    modalBackdrop: 1040,
    modal: 1050,
    popover: 1060,
    tooltip: 1070
  }
}

// Utilidades para trabajar con el tema
export const getThemeColor = (path) => {
  return path.split('.').reduce((obj, key) => obj?.[key], adminTheme.colors)
}

export const getThemeValue = (path) => {
  return path.split('.').reduce((obj, key) => obj?.[key], adminTheme)
}

// CSS custom properties para usar en componentes
export const getCSSCustomProperties = () => {
  return {
    '--admin-primary': adminTheme.colors.primary[500],
    '--admin-primary-hover': adminTheme.colors.primary[600],
    '--admin-sidebar-bg': adminTheme.sidebar.backgroundColor,
    '--admin-sidebar-text': adminTheme.sidebar.textColor,
    '--admin-header-height': adminTheme.header.height,
    '--admin-sidebar-width': adminTheme.sidebar.width.expanded,
    '--admin-sidebar-width-collapsed': adminTheme.sidebar.width.collapsed
  }
}
