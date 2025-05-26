# RedSYS Project : "Smart Task Assistant"

Una pequeña aplicación web que actúa como asistente de tareas automatizadas, con componentes de IA y automatización web (Selenium), que expone una API REST y permite realizar tareas como:

- Extraer precios/productos de una web.
- Analizar los datos con un modelo simple.
- Mostrar resultados en una pequeña interfaz web.
- Proveer endpoints para consumir los datos.

### 📦 Módulos y tecnologías utilizadas

| Módulo | Descripción | Tecnologías involucradas |
| --- | --- | --- |
| `scraper/` | Automatización web para recoger datos reales (ej. precios de productos) | **Python + Selenium** |
| `ml/` | Análisis simple con IA (ej. regresión para prever cambios de precios, clustering por categorías) | **Python + scikit-learn / pandas / numpy** |
| `api/` | Backend con API REST que expone los datos analizados | **Flask / FastAPI + GIT + Swagger opcional** |
| `frontend/` | Interfaz sencilla para ver los resultados (lista de productos, gráfico de evolución, etc.) | **HTML + Bootstrap + JS simple / jQuery (deseable)** |
| `db/` | Persistencia mínima en SQLite o PostgreSQL (simulado localmente) | **SQL / SQLAlchemy** |
| `tests/` | Tests automatizados básicos + integración de pytest + README | **pytest + unittest + CI básico (GitHub Actions opcional)** |

### ✨ Bonus opcional

- Usa Git con commits bien redactados y ramas si puedes.
- Sube una versión con documentación en `README.md` y capturas o GIF de funcionamiento.
- Estructura limpia tipo `src/`, con módulos bien separados y `requirements.txt`.

### ✅ Qué demuestras

| Habilidad | Cómo la demuestras |
| --- | --- |
| Python + librerías | Toda la lógica está en Python |
| Selenium | Scrap de datos reales con automatización web |
| IA | Modelo simple de machine learning aplicado a datos recogidos |
| API REST | Exposición de endpoints con FastAPI o Flask |
| Backend y frontend | Comunicación básica entre ambos lados |
| GIT y Clean Code | Estructura modular, bien documentada, con buenas prácticas |
| SQL / PostgreSQL | Conexión a una DB y persistencia mínima |
| Herramientas Agile | README con descripción de tareas, flujo de trabajo, pasos, etc. |

## 🧩 MÓDULO 1 — **Scraper con Selenium**

### 🎯 Objetivo

Automatizar la navegación y extracción de datos de una web sencilla (por ejemplo, precios y nombres de productos de Amazon, Wikipedia, etc.) y guardar los resultados en un archivo CSV o estructura de datos (como `pandas.DataFrame`).

## 🧰 Tecnologías usadas en este módulo

| Tecnología | Uso |
| --- | --- |
| **Python 3.8+** | Lenguaje principal del proyecto |
| **Selenium** | Automatización de navegador (scraping de sitios dinámicos) |
| **pandas** | Organización y análisis estructurado de los datos extraídos |
| **ChromeDriver** | Driver del navegador necesario para Selenium |
| **Entorno virtual (`venv`)** | Para aislar dependencias |
| **VS Code** (opcional) | Editor de código recomendado, sin automatismos externos |
|  |  |

## 🛠️ Pasos de instalación y preparación

### 1️⃣ Instalar Python 3.8+ (si no lo tienes)

Comprueba la versión:

```bash
python --version
```

Si no está instalado o es < 3.8, instálalo desde: [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

### 2️⃣ Crear entorno virtual

Un **entorno virtual** es una carpeta aislada donde se instalan **solo las librerías necesarias para tu proyecto actual**, sin afectar a otras instalaciones globales de Python en tu sistema.

> Es como tener un mini-Python y su propio conjunto de herramientas para ese proyecto específico.
> 

- 🎯 ¿Por qué usamos un entorno virtual?
    
    
    | Motivo | Explicación |
    | --- | --- |
    | ✅ **Aislamiento de dependencias** | Evita conflictos entre versiones de librerías usadas en distintos proyectos. |
    | ✅ **Reproducibilidad** | Puedes congelar las dependencias en un `requirements.txt`, y cualquiera podrá instalar las mismas versiones exactas. |
    | ✅ **Evita usar `pip` global** | No ensucias tu instalación de Python global con librerías que solo usa este proyecto. |
    | ✅ **Buenas prácticas profesionales** | En cualquier trabajo serio con Python, usarás entornos virtuales. |
    | ✅ **Evita errores sutiles** | Por ejemplo, si un proyecto requiere `pandas==1.3` y otro `pandas==2.0`, puedes tener ambas versiones, cada una en su entorno virtual. |

Esto te ayuda a aislar las librerías del proyecto:

```bash
python -m venv venv
```

Activar entorno virtual:

- En **Windows**:
    
    ```bash
    venv\Scripts\activate
    ```
    

---

### 3️⃣ Instalar librerías necesarias

Con el entorno virtual activo, ejecuta:

```bash
pip install selenium pandas
```

> 🔍 selenium para navegar automáticamente; pandas para organizar los datos.
> 

---

Puedes verificar que se instalaron correctamente con:

```bash
pip list
```

Deberías ver algo como:

```
Package    Version
---------- -------
pandas     2.x.x
selenium   4.x.x
```

### 4️⃣ Instalar ChromeDriver (manual o automatizado)

### Opción A: Instalación manual (recomendada para aprender)

1. Averigua tu versión de Google Chrome.
2. Ve a: https://sites.google.com/chromium.org/driver/
3. Descarga la versión que coincide con tu navegador.
4. Descomprime el binario.
5. Coloca el ejecutable en la carpeta del proyecto o en una carpeta incluida en el `PATH`.

### Opción B: Instalación automática (más fácil)

Si lo prefieres más directo:

```bash
pip install webdriver-manager
```

Y luego en el script:

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
```

### Crear la estructura de archivo

### 📁 Estructura sugerida

```
smart-task-assistant/
├── api/
│   └── main.py
├── scraper/
│   └── fetch_data.py
├── ml/
│   └── analyze.py
├── frontend/
│   └── index.html
├── db/
│   └── models.py
├── tests/
│   └── test_endpoints.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Continuamos instalando Git y subiendo nuestro proyecto a Github
---

## 🛠️ Guía para subir el proyecto a GitHub

### 1. Crear cuenta en GitHub

📎 Accede a [https://github.com/join](https://github.com/join)

Completa el formulario:
- **Username:** usa algo profesional (ej. `jesusmartinezdev`, `jmmin`, `jesus-martinez`).
- **Email:** preferiblemente uno que uses para temas técnicos o laborales.
- **Password:** segura y única.
- Verifica tu cuenta con el CAPTCHA.
- Elige el plan gratuito.

---

### 2. Configura tu perfil

Una vez dentro:
- ✅ Sube una foto profesional.
- ✅ Rellena tu bio (ej: *"Ingeniero informático. Apasionado por la IA, la automatización y el desarrollo limpio."*)
- ✅ Añade tu LinkedIn, portfolio o email.
- ✅ Ubicación opcional (Córdoba, España por ejemplo).

---

### 3. Crear el repositorio

📎 Accede a [https://github.com/new](https://github.com/new)

Completa así:

| Campo             | Valor sugerido                                                  |
|------------------|------------------------------------------------------------------|
| Repository name  | `smart-task-assistant`                                          |
| Description      | Proyecto demostrativo Python para automatización, scraping e IA |
| Visibility       | Public (para que puedan verlo los reclutadores)                 |
| Inicialización   | ❌ NO marques Add README, .gitignore o licencia                 |

Haz clic en **Create repository**.

---

### 4. Conecta tu repositorio local al remoto

En tu terminal, dentro del directorio del proyecto:

```bash
git init
git add .
git commit -m "Commit inicial: Describe que hiciste"
git remote add origin https://github.com/tu_usuario/smart-task-assistant.git
git branch -M main
git push -u origin main
```

⚠️ Sustituye `tu_usuario` por tu nombre de usuario real de GitHub.
