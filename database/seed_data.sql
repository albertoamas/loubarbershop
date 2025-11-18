-- Low Barber - Datos de Prueba
-- Datos iniciales para testing y desarrollo
-- Ejecutar después de schema.sql:
-- psql -U postgres -d lowbarber_db -f seed_data.sql

-- Limpiar datos existentes (opcional, comentar si no se desea)
-- TRUNCATE TABLE reservations, barber_services, products, services, barbers, users CASCADE;

-- ==========================================
-- 1. USUARIOS DE PRUEBA
-- ==========================================

-- Admin principal (contraseña: admin123)
INSERT INTO users (id, nombre, email, telefono, password_hash, rol, activo, email_verificado) 
VALUES (
    'admin-001',
    'Administrador Sistema',
    'admin@lowbarber.com',
    '+591 70000001',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5dkvJOqCQy00C', -- admin123
    'admin',
    TRUE,
    TRUE
) ON CONFLICT (id) DO NOTHING;

-- Cliente de prueba (contraseña: cliente123)
INSERT INTO users (id, nombre, email, telefono, password_hash, rol, activo, email_verificado) 
VALUES (
    'cliente-001',
    'Juan Pérez',
    'juan.perez@email.com',
    '+591 70000002',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5dkvJOqCQy00D', -- cliente123
    'cliente',
    TRUE,
    TRUE
) ON CONFLICT (id) DO NOTHING;

-- Usuarios para barberos (contraseña: barbero123)
INSERT INTO users (id, nombre, email, telefono, password_hash, rol, activo, email_verificado) 
VALUES 
    ('barbero-user-001', 'Carlos Mendoza', 'carlos.mendoza@lowbarber.com', '+591 70000003', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5dkvJOqCQy00E', 'barbero', TRUE, TRUE),
    ('barbero-user-002', 'Luis Rodríguez', 'luis.rodriguez@lowbarber.com', '+591 70000004', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5dkvJOqCQy00F', 'barbero', TRUE, TRUE),
    ('barbero-user-003', 'Miguel Torres', 'miguel.torres@lowbarber.com', '+591 70000005', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5dkvJOqCQy00G', 'barbero', TRUE, TRUE)
ON CONFLICT (id) DO NOTHING;

-- ==========================================
-- 2. BARBEROS
-- ==========================================

INSERT INTO barbers (id, nombre, especialidad, descripcion, experiencia_anos, disponible, activo, user_id, horario_trabajo)
VALUES
    (
        'barber-001',
        'Carlos Mendoza',
        'Especialista en cortes modernos',
        'Experto en fade, undercut y diseños creativos',
        5,
        TRUE,
        TRUE,
        'barbero-user-001',
        '{"lunes": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "martes": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "miércoles": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "jueves": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "viernes": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "sábado": {"activo": true, "inicio": "09:00", "fin": "14:00"}, "domingo": {"activo": false, "inicio": "09:00", "fin": "14:00"}}'
    ),
    (
        'barber-002',
        'Luis Rodríguez',
        'Barba y Bigote',
        'Especialista en perfilado y diseño de barbas',
        7,
        TRUE,
        TRUE,
        'barbero-user-002',
        '{"lunes": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "martes": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "miércoles": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "jueves": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "viernes": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "sábado": {"activo": true, "inicio": "09:00", "fin": "14:00"}, "domingo": {"activo": false, "inicio": "09:00", "fin": "14:00"}}'
    ),
    (
        'barber-003',
        'Miguel Torres',
        'Cortes Clásicos',
        'Maestro en técnicas tradicionales de barbería',
        10,
        TRUE,
        TRUE,
        'barbero-user-003',
        '{"lunes": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "martes": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "miércoles": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "jueves": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "viernes": {"activo": true, "inicio": "09:00", "fin": "18:00"}, "sábado": {"activo": true, "inicio": "09:00", "fin": "14:00"}, "domingo": {"activo": false, "inicio": "09:00", "fin": "14:00"}}'
    )
ON CONFLICT (id) DO NOTHING;

-- ==========================================
-- 3. SERVICIOS
-- ==========================================

INSERT INTO services (id, nombre, descripcion, precio, duracion, activo, popular, categoria, imagen_url)
VALUES
    -- CORTES
    ('service-001', 'Corte Clásico', 'Corte tradicional con tijera y máquina', 30000.00, 30, TRUE, TRUE, 'cortes', NULL),
    ('service-002', 'Corte Fade', 'Degradado profesional con acabado impecable', 40000.00, 45, TRUE, TRUE, 'cortes', NULL),
    ('service-003', 'Corte Undercut', 'Estilo moderno con contraste marcado', 45000.00, 45, TRUE, FALSE, 'cortes', NULL),
    ('service-004', 'Corte + Diseño', 'Corte con diseños personalizados', 50000.00, 60, TRUE, TRUE, 'cortes', NULL),
    
    -- BARBAS
    ('service-005', 'Perfilado de Barba', 'Perfilado y recorte de barba', 25000.00, 20, TRUE, FALSE, 'barbas', NULL),
    ('service-006', 'Barba Completa', 'Arreglo completo con máquina y navaja', 35000.00, 30, TRUE, TRUE, 'barbas', NULL),
    ('service-007', 'Afeitado Tradicional', 'Afeitado clásico con navaja y toalla caliente', 40000.00, 40, TRUE, FALSE, 'barbas', NULL),
    
    -- TRATAMIENTOS
    ('service-008', 'Tratamiento Capilar', 'Hidratación y nutrición del cabello', 35000.00, 30, TRUE, FALSE, 'tratamientos', NULL),
    ('service-009', 'Limpieza Facial', 'Limpieza profunda facial masculina', 45000.00, 40, TRUE, FALSE, 'tratamientos', NULL),
    ('service-010', 'Cejas', 'Perfilado y arreglo de cejas', 15000.00, 15, TRUE, FALSE, 'tratamientos', NULL),
    
    -- COMBOS
    ('service-011', 'Combo Clásico', 'Corte + Barba + Cejas', 65000.00, 60, TRUE, TRUE, 'combos', NULL),
    ('service-012', 'Combo Premium', 'Corte + Barba + Limpieza Facial', 95000.00, 90, TRUE, TRUE, 'combos', NULL),
    ('service-013', 'Combo Completo', 'Corte + Barba + Tratamiento Capilar + Cejas', 110000.00, 120, TRUE, FALSE, 'combos', NULL)
ON CONFLICT (id) DO NOTHING;

-- ==========================================
-- 4. RELACIÓN BARBEROS - SERVICIOS
-- ==========================================

-- Carlos Mendoza - Especialista en cortes
INSERT INTO barber_services (barber_id, service_id)
VALUES
    ('barber-001', 'service-001'), -- Corte Clásico
    ('barber-001', 'service-002'), -- Corte Fade
    ('barber-001', 'service-003'), -- Corte Undercut
    ('barber-001', 'service-004'), -- Corte + Diseño
    ('barber-001', 'service-010'), -- Cejas
    ('barber-001', 'service-011')  -- Combo Clásico
ON CONFLICT DO NOTHING;

-- Luis Rodríguez - Especialista en barbas
INSERT INTO barber_services (barber_id, service_id)
VALUES
    ('barber-002', 'service-001'), -- Corte Clásico
    ('barber-002', 'service-005'), -- Perfilado de Barba
    ('barber-002', 'service-006'), -- Barba Completa
    ('barber-002', 'service-007'), -- Afeitado Tradicional
    ('barber-002', 'service-011'), -- Combo Clásico
    ('barber-002', 'service-012')  -- Combo Premium
ON CONFLICT DO NOTHING;

-- Miguel Torres - Maestro en todos los servicios
INSERT INTO barber_services (barber_id, service_id)
VALUES
    ('barber-003', 'service-001'), -- Corte Clásico
    ('barber-003', 'service-002'), -- Corte Fade
    ('barber-003', 'service-003'), -- Corte Undercut
    ('barber-003', 'service-005'), -- Perfilado de Barba
    ('barber-003', 'service-006'), -- Barba Completa
    ('barber-003', 'service-008'), -- Tratamiento Capilar
    ('barber-003', 'service-009'), -- Limpieza Facial
    ('barber-003', 'service-011'), -- Combo Clásico
    ('barber-003', 'service-012'), -- Combo Premium
    ('barber-003', 'service-013')  -- Combo Completo
ON CONFLICT DO NOTHING;

-- ==========================================
-- 5. PRODUCTOS (OPCIONAL)
-- ==========================================

INSERT INTO products (id, nombre, descripcion, precio, stock, stock_minimo, categoria, marca, activo, destacado, sku)
VALUES
    ('product-001', 'Cera para Cabello', 'Cera de fijación fuerte', 35000.00, 50, 10, 'styling', 'American Crew', TRUE, TRUE, 'AC-WAX-001'),
    ('product-002', 'Aceite para Barba', 'Aceite hidratante natural', 45000.00, 30, 5, 'barba', 'Beardbrand', TRUE, TRUE, 'BB-OIL-001'),
    ('product-003', 'Shampoo Premium', 'Shampoo para cabello masculino', 40000.00, 40, 10, 'cuidado', 'Redken', TRUE, FALSE, 'RK-SHP-001')
ON CONFLICT (id) DO NOTHING;

-- ==========================================
-- 6. RESERVAS DE PRUEBA
-- ==========================================

-- Reserva pendiente
INSERT INTO reservations (id, user_id, barber_id, service_id, fecha_reserva, hora_inicio, hora_fin, estado, precio_final, cliente_nombre, cliente_telefono, cliente_email)
VALUES
    ('reservation-001', 'cliente-001', 'barber-001', 'service-001', CURRENT_DATE + INTERVAL '1 day', '10:00', '10:30', 'pendiente', 30000.00, 'Juan Pérez', '+591 70000002', 'juan.perez@email.com')
ON CONFLICT (id) DO NOTHING;

-- Reserva confirmada
INSERT INTO reservations (id, user_id, barber_id, service_id, fecha_reserva, hora_inicio, hora_fin, estado, precio_final, cliente_nombre, cliente_telefono, cliente_email, fecha_confirmacion)
VALUES
    ('reservation-002', 'cliente-001', 'barber-002', 'service-011', CURRENT_DATE + INTERVAL '2 days', '14:00', '15:00', 'confirmada', 65000.00, 'Juan Pérez', '+591 70000002', 'juan.perez@email.com', CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;

-- ==========================================
-- COMPLETADO
-- ==========================================

COMMIT;

SELECT 'Datos de prueba cargados exitosamente!' AS resultado;
