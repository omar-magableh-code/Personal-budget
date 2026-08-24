import streamlit as st
from user import user1
from budget import budget
import pandas as pd
# -----------# APP #------------
st.set_page_config(page_title="Personal Budget", page_icon="icon.jpg", layout="wide")

import base64
video_path =video_path = "Budget.mp4"
with open(video_path, "rb") as video_file:
    video_bytes = video_file.read()

video_base64 = base64.b64encode(video_bytes).decode()

st.markdown(
    f"""
    <style>
    .stApp {{
        background: transparent;
    }}

    video {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        z-index: -1;
        object-fit: cover;
    }}
    </style>

    <video autoplay loop muted>
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
    </video>

    """,
    unsafe_allow_html=True
)


st.markdown("""
<style>
label {
    color: white !important;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


st.title("Welcome to Your Budget Calculator                                   😊💸 ")
st.image("Money Business GIF by JustStartInvesting.gif")
# -----------#Session_stat#------------
if "page" not in st.session_state :
    st.session_state.page="login"
# -----------#Login #------------
if st.session_state.page =="login":
    st.subheader("login🔐")

    username=st.text_input("Enter Your Name : ",max_chars=10, key="login_username")
    password=st.text_input("Enter Your Password : ",type="password",max_chars=12,key="login_password")

    if st.button("login🔐") :
       result=user1.login(username,password)   
       if "Welcome" in result :
        st.session_state.page = "info"
        st.rerun()
       else :
           st.error("We Can't Faound your account,Creat a New account ➕👤 ") 

    if st.button("Sign Up ➕👤"):
        st.session_state.page = "signup"
        st.rerun() 
# -----------#Sgin Up#------------
if st.session_state.page == "signup":
   st.subheader("Create New Account 👤➕")
   username=st.text_input("Enter Your Name : ",max_chars=10, key="signup_username")
   password=st.text_input("Enter Your Password : ",type="password",max_chars=12,key="signup_password")
   if st.button("New Account 👤➕") :
     result=user1.sign_up(username,password)
     st.success(result)
     st.session_state.page = "login"
     st.rerun()


# -----------#P-Info#------------
if st.session_state.page=="info":
    st.subheader("Personal Information💁‍♂️🙆‍♂️.")
    age=st.slider("Enter Your Age : ",min_value=18,max_value=100,value=18)
    status=st.radio("Marital Status",["Single","Married"])
    gender=st.selectbox("What Your Gender ? ",[" ","Male","Female"])
    if st.button("Next ➡️"):
     st.session_state.age=age
     st.session_state.status=status
     st.session_state.gender=gender
     st.session_state.page = "budget"
     st.rerun()
# -----------#budget#------------
if st.session_state.page == "budget":
    st.subheader("Calculate Salary💸")
    salary=st.number_input("Enter Your Salary : ",max_value=20000,min_value=0) 
    increase=st.number_input("Enter Your Increase : ",min_value=0,max_value=20000)
    if st.button("Calculate 💰"):
        total = budget.cal_increase(salary, increase)
        st.success(f"Total Salary = {total} JD.")
    if st.button("Go To Expenses ➡️"):
        st.session_state.page = "Expense_account"
        st.rerun()

# -----------#Expense_account#------------
if st.session_state.page == "Expense_account":
   st.subheader("Expense Account 🎯💵")
   if st.session_state.status=="Single":
      apartment=st.number_input("Enter how much spend to apartment ",max_value=1700,min_value=100)
      clothes=st.number_input("Enter how much spend to buy new clothes ",max_value=900,min_value=0)
      car = 0
      public_transportation = 0

      transpotation=st.radio("Do you own a car or not ?",["Yes","No"])

      if transpotation == "Yes":
         car=st.number_input("how much you spend to your car monthly",max_value=400,min_value=0)

      else:
          public_transportation=st.number_input("Enter how much spend to public transportation ",max_value=100,min_value=0)
      travel=0
      travel=st.radio("Do you travel monthly?",[True,False])
      if travel == True :
        travel=st.number_input("How much do you spend on personal travel ?",min_value=0,max_value=2000)
      personal=budget.Personal_Expense(apartment,clothes,public_transportation,car,travel)   
      if st.button("Calculate 💰"):
         total = budget.remaining_salary_p()
         st.success(f"remaining salary persone = {total} JD.")
         if total <= (salary * 0.20):
                st.error("⚠️Warning: Your personal expenses exceed your total income!")
         else:
            st.success("✅Great! Your personal budget is safe.")
         data = {
            'Category': ['Apartment', 'Clothes', 'Transport', 'Travel'],
            'Cost': [apartment, clothes, car + public_transportation, travel if isinstance(travel, (int, float)) else 0]
        }
         df= pd.DataFrame(data)
         st.bar_chart(df.set_index('Category'))   

   else:
       school_installments=st.number_input("How much do you spend on school installments ?",max_value=850,min_value=0)
       university_fees=st.number_input("How much do you spend on university fees ?",max_value=850,min_value=0)
       home_bills=st.number_input("How much do you spend on the house (electricity, water, air conditioning, internet) ?",max_value=800,min_value=0)
       family=budget.family_Expense(school_installments,university_fees,home_bills)
       if st.button("Calculate 💰"):
                total = budget.remaining_salary_f()
                st.success(f"remaining salary family = {total} JD.")
                if total <= (salary * 0.20):
                   st.error("⚠️Warning: Your Family expenses exceed your total income!")
                else:
                  st.success("✅Great! Your Family budget is safe.")       

                family_data = {
                'Category': ['School', 'University', 'Home Bills'],
                'Cost': [school_installments, university_fees, home_bills]
            }
                df_family = pd.DataFrame(family_data)
                st.bar_chart(df_family.set_index('Category'))


