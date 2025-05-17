USE EXAMEN2DI;

-- Crear tablas con utf8mb4
CREATE TABLE IF NOT EXISTS usuarios (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(255) NOT NULL,
    contrasenia VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;


-- Tabla para almacenar las poblaciones disponibles
CREATE TABLE IF NOT EXISTS poblaciones (
    id_poblacion INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;


-- Tabla para almacenar las actividades extraescolares
CREATE TABLE IF NOT EXISTS actividades (
    id_actividad INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Tabla principal de estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    dni VARCHAR(9) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    id_poblacion INT NOT NULL,
    distancia_centro DECIMAL(5,2) NOT NULL,
    modalidad ENUM('Presencial', 'A Distancia') NOT NULL,
    usuario VARCHAR(50) NOT NULL,
    tutor VARCHAR(100),
    telefono_tutor VARCHAR(20),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_poblacion) REFERENCES poblaciones(id_poblacion)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Tabla para relacionar estudiantes con actividades (relación muchos a muchos)
CREATE TABLE IF NOT EXISTS estudiante_actividades (
    id_estudiante_actividad INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_actividad INT NOT NULL,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
    FOREIGN KEY (id_actividad) REFERENCES actividades(id_actividad),
    UNIQUE KEY (id_estudiante, id_actividad)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Añadir índice único para DNI después de crear la tabla
ALTER TABLE estudiantes ADD UNIQUE INDEX idx_dni_unique (dni);

-- Añadir índice único para usuario después de crear la tabla
ALTER TABLE estudiantes ADD UNIQUE INDEX idx_usuario_unique (usuario);

SET FOREIGN_KEY_CHECKS=0;

-- Insertar datos en tablas base

INSERT INTO usuarios (usuario, contrasenia) VALUES
('valentina', 'secreta'),
('hotel', 'Brianda23$');

-- Insertar las poblaciones que aparecen en el combobox
INSERT INTO poblaciones (nombre) VALUES 
('Guadalajara'), 
('Marchamalo'), 
('Yunquera'), 
('Horche'), 
('Torija');

-- Insertar las poblaciones que aparecen en la interfaz
INSERT INTO actividades (nombre) VALUES 
('Danza'), 
('Ajedrez'), 
('Fútbol');

-- EJEMPLOS

INSERT INTO estudiantes (nombre, apellidos, dni, fecha_nacimiento, id_poblacion, distancia_centro, modalidad, usuario, tutor, telefono_tutor) VALUES
('María', 'García López', '12345678A', '2005-03-15', 1, 2.5, 'Presencial', 'mgarci', 'Juan García Pérez', '611223344'),
('Carlos', 'Martínez Ruiz', '87654321B', '2010-07-22', 2, 5.0, 'A Distancia', 'cmarti', 'Ana Ruiz Sánchez', '622334455'),
('Laura', 'Fernández Gómez', '11223344C', '2002-11-30', 3, 1.2, 'Presencial', 'lfernan', NULL, NULL),
('Pedro', 'Sánchez Díaz', '22334455D', '2008-05-10', 4, 8.7, 'A Distancia', 'psanche', 'Luisa Díaz Méndez', '633445566'),
('Ana', 'Rodríguez Pérez', '33445566E', '2004-09-18', 5, 3.3, 'Presencial', 'arodri', NULL, NULL),
('Javier', 'López Martín', '44556677F', '2012-12-05', 2, 12.0, 'A Distancia', 'jlopez', 'Marta Martín García', '644556677'),
('Sofía', 'Gómez Hernández', '55667788G', '2003-04-25', 5, 0.5, 'Presencial', 'sherna', NULL, NULL),
('David', 'Díaz Jiménez', '66778899H', '2007-08-12', 1, 4.2, 'A Distancia', 'ddiaz', 'Elena Jiménez Ruiz', '655667788');

-- Insertar relaciones entre estudiantes y actividades
INSERT INTO estudiante_actividades (id_estudiante, id_actividad) VALUES
(1, 1), -- María García - Danza
(1, 3), -- María García - Fútbol
(2, 2), -- Carlos Martínez - Ajedrez
(3, 4), -- Laura Fernández - Baloncesto
(3, 5), -- Laura Fernández - Teatro
(4, 1), -- Pedro Sánchez - Danza
(4, 6), -- Pedro Sánchez - Música
(5, 3), -- Ana Rodríguez - Fútbol
(5, 5), -- Ana Rodríguez - Teatro
(6, 2), -- Javier López - Ajedrez
(6, 4), -- Javier López - Baloncesto
(7, 1), -- Sofía Gómez - Danza
(7, 6), -- Sofía Gómez - Música
(8, 3); -- David Díaz - Fútbol


SET FOREIGN_KEY_CHECKS=1;

