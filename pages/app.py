import streamlit as st

def calculate_price(plan, months):
    if plan == "Mensual":
        return 30 * months
    elif plan == "Cuatrimestral":
        return 100 * months
    elif plan == "Anual":
        return 300 * months
    else:
        return 0

def plan_entrenamiento():
    st.title("¡Elige tu Plan de Entrenamiento!")
    st.write("Bienvenido a nuestra plataforma de entrenamiento. ¡Selecciona el plan que mejor se adapte a ti y comienza a mejorar tu salud y bienestar!")

    plan = st.selectbox("Selecciona un plan", ["Mensual", "Cuatrimestral", "Anual"])
    months = st.number_input("Número de meses", min_value=1, max_value=12, value=1)

    price = calculate_price(plan, months)

    if price > 0:
        st.subheader("Resumen del Plan")
        st.write(f"**Plan seleccionado:** {plan}")
        st.write(f"**Duración del plan:** {months} meses")
        st.write(f"**Precio total:** ${price}")
        st.write("¡Comienza hoy mismo tu viaje hacia una vida más saludable!")
    else:
        st.warning("Por favor, selecciona un plan válido.")

def main():
    st.set_page_config(
        page_title="Ejemplos Streamlit",
        page_icon="🔥",
    )

    st.sidebar.title("Ejemplos Streamlit")
    app_selector = st.sidebar.radio("Selecciona una demo", ("Plan de Entrenamiento", "Demo de Animación", "Demo de Plotting", "Demo de Mapeo"))

    if app_selector == "Plan de Entrenamiento":
        plan_entrenamiento()
    elif app_selector == "Demo de Animación":
        animation_demo()
    elif app_selector == "Demo de Plotting":
        plotting_demo()
    elif app_selector == "Demo de Mapeo":
        mapping_demo()

if __name__ == "__main__":
    main()
