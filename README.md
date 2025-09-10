# 📝 Chuleta rápida: Entornos virtuales en VS Code

## 1. Crear entorno virtual
```bash
python -m venv .venv
```

## 2. Activar entorno (terminal integrada de VS Code)
- **Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```
- **Windows CMD**
```cmd
.\.venv\Scripts\activate
```
- **Linux/macOS**
```bash
source .venv/bin/activate
```

## 3. Seleccionar intérprete en VS Code
`Ctrl+Shift+P` → **Python: Select Interpreter** → elegir `.venv`.

## 4. Instalar dependencias
```bash
pip install -qU pip setuptools wheel
pip install -qU "langchain[google-genai]"
```

## 5. Guardar dependencias
```bash
pip freeze > requirements.txt
```

## 6. Desactivar entorno
```bash
deactivate
```
