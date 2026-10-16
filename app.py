import streamlit as st


def turkish_lower(text):
    return st.text.replace("İ", "i").replace("I", "ı").lower()


ALLERGENS = {
    "süt": "Milk", "peynir": "Milk", "yoğurt": "Milk", "tereyağ": "Milk",
    "yumurta": "Egg",
    "ekmek": "Gluten", "makarna": "Gluten", "baklava": "Gluten",
    "börek": "Gluten", "buğday": "Gluten",
    "fıstık": "Peanut or tree nut (check which one!)",
    "ceviz": "Tree nut", "fındık": "Tree nut", "badem": "Tree nut",
    "susam": "Sesame", "tahin": "Sesame",
    "balık": "Fish", "karides": "Shellfish", "midye": "Shellfish",
}

HALAL_RISK = {
    "domuz": "Contains pork",
    "jambon": "Ham, usually pork",
    "şarap": "Contains alcohol", "bira": "Contains alcohol",
    "rakı": "Contains alcohol",
    "jelatin": "Gelatin, source unknown",
    "sucuk": "Verify the meat type",
}


def find_matches(menu_line, knowledge_base):
    words = turkish_lower(menu_line).split()
    found = {}
    for word in words:
        for keyword, label in knowledge_base.items():
            if word.startswith(keyword):
                found[label] = word
    return found


st.title("🍽️ Menu Guard (prototype)")
menu_line = st.text_input("Type a menu item (Turkish):", "Sucuklu yumurta")

if menu_line:
    allergens = find_matches(menu_line, ALLERGENS)
    risks = find_matches(menu_line, HALAL_RISK)

    for label, trigger in allergens.items():
        st.warning(f"⚠️ Possible allergen: {label} (because of '{trigger}')")
    for label, trigger in risks.items():
        st.error(f"🕌 Halal check needed: {label} (because of '{trigger}')")

    if not allergens and not risks:
        st.info(
            "No known keyword found. This does NOT mean the dish is safe. "
            "Please ask the staff."
        )