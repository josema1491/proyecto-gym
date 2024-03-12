import streamlit as st

# Función para calcular el precio según el plan y el número de meses
def calculate_price(plan, months):
    if plan == "Mensual":
        return 30 * months
    elif plan == "Cuatrimestral":
        return 100 * months
    elif plan == "Anual":
        return 300 * months
    else:
        return 0

# Configuración de la página
st.set_page_config(page_title="Plan de Entrenamiento", page_icon="💪")

# Título y descripción
st.title("¡Elige tu Plan de Entrenamiento!")
st.write("Bienvenido a nuestra plataforma de entrenamiento. ¡Selecciona el plan que mejor se adapte a ti y comienza a mejorar tu salud y bienestar!")

# Selección del plan
plan = st.selectbox("Selecciona un plan", ["Mensual", "Cuatrimestral", "Anual"])

# Número de meses
months = st.number_input("Número de meses", min_value=1, max_value=12, value=1)

# Calcular el precio total
price = calculate_price(plan, months)

# Mostrar el precio total
if price > 0:
    st.subheader("Resumen del Plan")
    st.write(f"**Plan seleccionado:** {plan}")
    st.write(f"**Duración del plan:** {months} meses")
    st.write(f"**Precio total:** ${price}")
    st.write("¡Comienza hoy mismo tu viaje hacia una vida más saludable!")
else:
    st.warning("Por favor, selecciona un plan válido.")
