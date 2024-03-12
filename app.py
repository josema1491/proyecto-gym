# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def calculate_price(plan, months):
    if plan == "Mensual":
        return 30 * months
    elif plan == "Cuatrimestral":
        return 100 * months
    elif plan == "Anual":
        return 300 * months
    else:
        return 0

def run():
    st.set_page_config(
        page_title="Plan de Entrenamiento",
        page_icon="💪",
    )
    st.sidebar.markdown("[Plan de Entrenamiento](/)")
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


if __name__ == "__main__":
    run()
