import streamlit as st
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type

st.set_page_config(page_title="📱 Mobile Number Lookup", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>📞 Mobile Number Intelligence</h1>
    <p style='text-align: center; font-size: 18px;'>Analyze any mobile number using public information — clean, fast, and easy.</p>
    <hr style="border: 1px solid #ccc;">
""", unsafe_allow_html=True)

number = st.text_input("Enter Mobile Number with Country Code", placeholder="+923001234567")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Lookup Now"):
    try:
        parsed_number = phonenumbers.parse(number)

        if not phonenumbers.is_valid_number(parsed_number):
            st.warning("⚠️ The number entered is not valid. Please check the format.")
        else:
            location = geocoder.description_for_number(parsed_number, "en")
            sim_network = carrier.name_for_number(parsed_number, "en")
            time_zones = timezone.time_zones_for_number(parsed_number)
            number_category = number_type(parsed_number)

            number_type_map = {
                0: "Fixed Line",
                1: "Mobile",
                2: "Fixed Line or Mobile",
                3: "Toll Free",
                4: "Premium Rate",
                5: "Shared Cost",
                6: "VoIP",
                7: "Personal Number",
                8: "Pager",
                9: "Universal Access Number",
                10: "Voicemail",
                27: "Unknown"
            }

            st.success("✅ Number lookup completed successfully!")

            with st.container():
                st.markdown("### 🔎 Lookup Result")
                st.markdown(f"- **🌍 Location:** `{location}`")
                st.markdown(f"- **📡 Carrier/Network:** `{sim_network or 'Unknown'}`")
                st.markdown(f"- **🕒 Time Zone(s):** `{', '.join(time_zones)}`")
                st.markdown(f"- **📂 Number Type:** `{number_type_map.get(number_category, 'Unknown')}`")

    except:
        st.error("❌ Invalid input. Please enter a valid number with country code like +923001234567.")
