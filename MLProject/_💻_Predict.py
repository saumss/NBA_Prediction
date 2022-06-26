import pickle
import streamlit as st
import time
import sklearn

# loading in the model to predict on the data
pickle_model = open('MLProject/modelLogi.pkl', 'rb')
model = pickle.load(pickle_model)

def welcome():
    return 'welcome all'

# defining the function which will make the prediction using
# the data which the user inputs
def prediction(elo_n_pred, elo_i_pred, forecast):
    prediction = model.predict(
        [[elo_n_pred, elo_i_pred, forecast]])
    print(prediction)
    return prediction

def main():

    html_temp = """
	<div style ="background-color:lightblue;padding:13px">
	  <h1 style ="color:black;text-align:center;">Streamlit NBA Game Outcome App </h1>
	</div>
	<br>
	"""
    st.markdown(html_temp, unsafe_allow_html=True)

    hide_menu_style = """
    <style>
    
    footer {visibility: hidden; }
    </style>
    """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    elo_i_pred = st.slider("Elo Rating (International):", 0.00, 1.00)
    elo_n_pred = st.slider("Elo Rating (National):", 0.00, 1.00)
    forecast = st.slider("Forecast:", 0.00, 1.00)
    gameresult = ""

    if st.button("Predict"):
        gameresult = prediction(elo_n_pred, elo_i_pred, forecast)
        with st.spinner("Loading..."):
            time.sleep(5)
    if gameresult == 1:
        st.success('The Team will: win')
        st.balloons()
    if gameresult == 0:
           st.warning('The Team will: lose')

if __name__ == '__main__':
    main()
html_temp1 = """
	<br>
	<br>
	<br>
	<br>
	<div>
	  <p style ="color:grey;text-align:right;">github/saumss/NBA_Prediction </p>
	</div>
"""
st.markdown(html_temp1, unsafe_allow_html=True)
