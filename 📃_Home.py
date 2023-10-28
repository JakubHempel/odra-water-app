import streamlit as st

st.set_page_config(layout="wide")

# Customize page title
st.title(
    "Witaj w OdrApp! 💦"
)

st.markdown(
    """
    ***OdrApp*** to aplikacja służąca do monitoringu jakości wody w rzece Odra. Przedstawia ona wieloczasową analiza jakości wody z wykorzystaniem zobrazowań satelitarnych i Google Earth Engine. Obejmuje okres od 2018 do teraz, od kwietnia do października.
    Eksploruj wszystkie strony do woli i dowiedz się więcej o zanieczyszczeniu wody w Odrze.
    """)

st.divider()

st.markdown("""
    #### Sugerowane działania:
    1. Przejdź do strony *Indexes* 🌍 i dowiedz się więcej o indekach spektralnych użytych w analizie.
    2. Odwiedzaj strony indeksów:
        - 💦 - powszechnie stosowane wskaźniki,
        - 🦠 - związane stricte z zanieczyszczeniem i jakością wody.\n
        Przeglądaj mapy z wizualizacją indeksów w zakładce 🗺️ Map i wykres liniowy przedstawiający średnią wartość indeksów na przestrzeni analizowanego okresu w zakładce 📈 Chart.
    3. Wejdź na stronę *Charts* 📈 gdzie poznasz wizualizację wyników na wykresach, tj.
        - "roczne",
        - "miesięczne",
        - okresowe,
        - z katastrofy ekologicznej Odry 2022.
    4. Na stronie *Disaster Odra 2022* znajdziesz rozszerzoną analizę jakości wody w 4 nadrzecznych miastach: Ostravie (CZ), Wrocławiu, Frankfurcie (DE) oraz Szczecinie.

    **Kolejność dowolna! Na start, pamiętaj o przeczytaniu o indeksach spektralnych na stronie *Indexes* 🌍.**

    ##### Miłego korzystania! 💦
    """
)
