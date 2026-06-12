import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("🚀 Iniciando suite de pruebas funcionales automatizadas...")

# Abrir el navegador Chrome automáticamente
driver = webdriver.Chrome()

try:
    # 1. Conectarse al servidor local (Módulo Principal)
    URL_LOCAL = "http://127.0.0.1:5000"
    print("🌍 Navegando hacia la Página Principal...")
    driver.get(URL_LOCAL)
    driver.maximize_window()
    time.sleep(2) # Pausa para registrar la captura visual
    
    # 2. Probar el botón de navegación del Home
    print("🖱️ Dando clic en el botón 'Abrir Módulo de Reseñas'...")
    btn_navegar = driver.find_element(By.ID, "btn_navegar")
    btn_navegar.click()
    time.sleep(2)
    
    # 3. Rellenar el formulario automáticamente (Inyección de datos)
    print("✍️ Inyectando datos en el formulario de registro...")
    driver.find_element(By.ID, "equipo").send_keys("Tarjeta Gráfica ASUS RTX 4060")
    driver.find_element(By.ID, "categoria").send_keys("Componentes")
    
    # Limpiar el número por defecto y poner un 5
    campo_calif = driver.find_element(By.ID, "calificacion")
    campo_calif.clear()
    campo_calif.send_keys("5")
    
    driver.find_element(By.ID, "comentario").send_keys(
        "Prueba de automatización exitosa. El componente mantiene temperaturas estables bajo estrés simulado."
    )
    time.sleep(2)
    
    # 4. Enviar el formulario
    print("🖱️ Pulsando el botón 'Guardar Reseña en la Nube'...")
    driver.find_element(By.ID, "btn_guardar").click()
    time.sleep(4) # Esperamos a que viaje a Render y regrese
    
    # 5. Auditoría del DOM: Verificar si se guardó e hizo la consulta
    print("🔍 Buscando confirmación del registro en la pantalla...")
    codigo_fuente = driver.page_source
    texto_esperado = "¡Análisis de hardware guardado correctamente en PostgreSQL!"
    
    print("\n================ REPORTES FINALES DE QA ================")
    if texto_esperado in codigo_fuente:
        print("✅ VEREDICTO: [PASSED / EXITOSO]")
        print("📝 Detalle: Los datos se guardaron en Render y se consultaron abajo correctamente.")
    else:
        print("❌ VEREDICTO: [FAILED / FALLIDO]")
        print("📝 Detalle: El banner de éxito no apareció en la interfaz.")
    print("========================================================\n")

except Exception as e:
    print(f"⚠️ Error durante la ejecución de la prueba: {e}")
finally:
    print("🔌 Cerrando el navegador de pruebas.")
    driver.quit()