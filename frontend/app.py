import requests
import time
import streamlit as st

input_data_features = [
    "social_energy", "alone_time_preference", "talkativeness", "deep_reflection", "group_comfort", "party_liking", 
    "listening_skill", "empathy", "creativity", "organization", "leadership", "risk_taking", "public_speaking_comfort", 
    "curiosity", "routine_preference", "excitement_seeking", "friendliness", "emotional_stability", "planning", 
    "spontaneity", "adventurousness", "reading_habit", "sports_interest", "online_social_usage", "travel_desire", 
    "gadget_usage", "work_style_collaborative", "decision_speed", "stress_handling"
]
FASTAPI_URL = "http://localhost:8000/predict"

if "page" not in st.session_state:
    st.session_state.page = 0
    
if "submitted" not in st.session_state:
    st.session_state.submitted = False

for feature in input_data_features:
    if feature not in st.session_state:
        st.session_state[feature] = 5  

features_per_page = 4
total_no_of_pages = len(input_data_features) // features_per_page

def next():
    if st.session_state.page < total_no_of_pages:
        st.session_state.page += 1

def prev():
    if st.session_state.page > 0:
        st.session_state.page -= 1

def reset():
    for feature in input_data_features:
        st.session_state[feature] = 5
    st.session_state.page = 0
    st.session_state.submitted = False

def main():
    start_index = st.session_state.page * features_per_page
    end_index = start_index + features_per_page
    current_features = input_data_features[start_index:end_index]

    st.markdown("## Personality type detection")

    if not st.session_state.submitted:
        st.write("Rate your behavioural and psychological characteristics on a scale of 1 to 10.")

        st.progress(st.session_state.page / total_no_of_pages)
        st.divider()

        for feature in current_features:
            value = st.slider(label=feature.replace("_", " ").capitalize(), min_value=1, max_value=10, 
                    value=st.session_state[feature])
            st.session_state[feature] = value

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.session_state.page > 0:
                    st.button("Previous", on_click=prev, use_container_width=True, disabled=st.session_state.submitted)
        with col2:
            st.write(f"Questions answered: {(st.session_state.page * features_per_page) + len(current_features)} / {len(input_data_features)}")
        with col3:
            if st.session_state.page < total_no_of_pages:
                st.button("Next", on_click=next, use_container_width=True)
            else:
                st.button("Submit", use_container_width=True, disabled=st.session_state.submitted)
                st.session_state.submitted = True
    else:
        # Send request to backend
        input_data = {feature: st.session_state[feature] for feature in input_data_features}
        with st.spinner("Sending request to backend..."):
            time.sleep(1)  
            try:
                response = requests.post(FASTAPI_URL, json=input_data)
                if response.status_code == 200:
                    result = response.json()
                    if response:
                        st.balloons()
                        st.success("Successfully received prediction")
                        st.markdown(f"#### Predicted Personality Type: {result['predicted_personality']}")
                        col1, space1, col2, space2, col3 = st.columns([2, 1, 2, 1, 2])
                        with col1:
                            st.metric("Ambivert", result['ambivert_percent'])
                        with col2:
                            st.metric("Extrovert", result['extrovert_percent'])
                        with col3:
                            st.metric("Introvert", result['introvert_percent'])
                else:
                    st.error("Failed to get a valid response from the server.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

        # Hide the Previous and Submit buttons after submission and response
        st.button("Reset", on_click=reset, use_container_width=True)

if __name__ == "__main__":
    main()
