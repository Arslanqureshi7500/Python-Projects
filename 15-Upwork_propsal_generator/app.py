"""
Import Streamlit library for building interactive web applications and OpenAI library for accessing OpenAI's APIs.

Parameters:
    st (module): Streamlit library for building web applications.
    OpenAI (module): OpenAI library for accessing OpenAI's APIs.

Returns:
    None

Example:
    import streamlit as st
    from openai import OpenAI
"""

import streamlit as st
from openai import OpenAI

def login():
    """
        Function to handle user login functionality for the "AI Winning Proposal Generator" application
        This function checks if the user has an account, 
        if not, it allows the user to create one. 
        It then prompts the user to login with their credentials. 
        If the login is successful, the function returns True, indicating the user is logged in 
        and can proceed further.
        If the login fails or the user has not created an account,the function returns False.
        Returns:
            bool: True if the user is logged in successfully, False otherwise.

        Example:
            >>> login()
    """
            
    # Check if user has an account
    if "username" not in st.session_state:
        st.session_state["username"] = ""  # Initialize username attribute
        st.session_state["password"] = ""  # Initialize password attribute
        st.session_state["logged_in"] = False  # Initialize logged_in attribute
        st.session_state["account_created"] = False  # Initialize account_created attribute

    st.title("AI Winning Proposal Generator")  # Set title for the application
    st.image("cover_pic.jpg", use_column_width=True)  # Add cover picture
    st.write("Please login to your account to generate winning proposals.")  # Display login prompt


    if not st.session_state.logged_in:
        st.sidebar.header("Create Account")  # Display header for creating account
        new_username = st.sidebar.text_input("New Username")  # Input field for new username
        new_password = st.sidebar.text_input("New Password", type="password")  # Input field for new password
        confirm_password = st.sidebar.text_input("Confirm Password", type="password")  # Input field for confirming password
        if st.sidebar.button("Create Account"):  # Button to create account
            if new_password != confirm_password:  # Check if passwords match
                st.sidebar.error("Passwords do not match")  # Display error message if passwords don't match
            elif new_username and new_password:  # Check if username and password are provided
                st.session_state.username = new_username  # Store new username
                st.session_state.password = new_password  # Store new password
                st.session_state.account_created = True  # Flag to indicate account creation
                st.sidebar.success("Account created successfully! You can now login.")  # Display success message
                st.balloons()

        st.sidebar.header("Login")  # Display header for login section
        username = st.sidebar.text_input("Username", st.session_state.username)  # Input field for username
        password = st.sidebar.text_input("Password", type="password", value=st.session_state.password)  # Input field for password

        if st.sidebar.button("Login"):  # Button for login
            # Check login credentials
            if username == st.session_state.username and password == st.session_state.password:
                st.session_state.logged_in = True  # Set logged_in flag to True
                return True  # Return True to indicate successful login
            else:
                st.sidebar.error("Invalid username or password")  # Display error message for invalid credentials

        if st.session_state.account_created:  # Check if account was just created
            st.session_state.account_created = False  # Reset the flag
            st.sidebar.header("Login with Newly Created Account")  # Display header for logging in with newly created account
            st.sidebar.info("Please login with the newly created account.")  # Display info message
            st.session_state.username = new_username  # Store newly created username for login
            st.session_state.password = new_password  # Store newly created password for login
            return False  # Don't proceed further unless user logs in

    else:  # If logged in, show logout button
        if st.sidebar.button("Logout"):  # Button for logout
            st.session_state.clear()  # Clear session state on logout
        return True  # Continue further if user is logged in

    return False  # If not logged in or account not created, don't proceed further


def about_us():
    """
    Function to display information about the project, supervisor, and students.
    This function sets the title of the page to "About Us" 
    and displays various sections including project features, supervisor information, and student information.

    Parameters:
        None

    Returns:
        None

    Example:
        >>> about_us()
    """

    st.title("About Us")  # Set title for the page
    st.header("Project Features")  # Display header for project features
    st.write("""
    - AI Winning Proposal Generator helps you to create winning proposals for your clients.
    - It uses state-of-the-art AI models to generate customized proposals based on the client's project description.
    - You can customize the proposal by providing your name, expertise, and client project details.
    - The system provides helpful prompts and suggestions to craft compelling proposals that stand out.
    """)  # Write project features

    st.image("cover2.jpg", caption='')  # Display cover image
    st.markdown("<h1 style='text-align: center; color: green;'>Supervisor</h1>", unsafe_allow_html=True)  # Display heading for supervisor
    left_co, cent_co,last_co = st.columns(3)  # Divide into three columns
    with cent_co:
        st.image("passport size pic.jpg", caption='')  # Display supervisor's image
    # st.image("passport size pic.jpg", caption='')  # Display supervisor's image
    st.markdown("<h3 style='text-align: center; color: green;'>Mr. Waqas ALi</h3>", unsafe_allow_html=True)  # Display supervisor's name
    st.markdown("<h3 style='text-align: center; color: green;'>Data Scientist</h3>", unsafe_allow_html=True)  # Display supervisor's designation
    st.markdown("<h3 style='text-align: center; color: green;'>Digitech and Habibi Group </h3>", unsafe_allow_html=True)  # Display supervisor's institution

    col1, col2 = st.columns(2)  # Divide into two columns
    with col1:
        st.header("Student Information")  # Display header for student information
        st.image("passport size pic.jpg", caption='')  # Display student's image
        st.write("Student Name: Muhammad Arslan Qureshi")  # Display student's name
        st.write("Registration No. *********** ")  # Display student's registration number
        st.write("Registration No. BS Information Technology ")  # Display student's degree
        st.write("Section Morning")  # Display student's section
        st.write("Session: Fall 2015 - 2019")  # Display session
        st.write("Email: Arslanqureshi7500@gmail.com")  # Display student's email
        st.write("Phone: +923077600650")  # Display student's phone number

    with col2:
        st.header("Student Information")  # Display header for student information
        st.image("passport size pic.jpg", caption='')  # Display student's image
        st.write("Student Name: Muhammad Arslan Qureshi")  # Display student's name
        st.write("Registration No. *********** ")  # Display student's registration number
        st.write("Registration No. BS Information Technology ")  # Display student's degree
        st.write("Section Morning")  # Display student's section
        st.write("Session: Fall 2015 - 2019")  # Display session
        st.write("Email: Arslanqureshi7500@gmail.com")  # Display student's email
        st.write("Phone: +923077600650")  # Display student's phone number



def main():
    """
    Main function to control the flow of the application and handle user interactions.

    This function allows users to navigate between different pages ("Home" and "About Us"),
    login, submit API key, and generate proposals.

    Parameters:
        None

    Returns:
        None

    Example:
        >>> main()
    """

    menu = ["Home", "About Us"]  # Define menu options
    choice = st.sidebar.selectbox("Navigation", menu)  # Create a selectbox for navigation

    if choice == "Home":  # If user selects "Home"
        if login():  # Check if user is logged in
            if "api_key" not in st.session_state:
                st.session_state["api_key"] = ""  # Initialize api_key attribute

            st.sidebar.header("API Key")  # Display header for API Key section
            api_key = st.sidebar.text_input("Please enter your API_KEY", value=st.session_state.api_key)  # Input field for API key
            if st.sidebar.button("Submit API Key"):  # Button to submit API key
                st.session_state.api_key = api_key  # Store API key in session state

            base_url = "https://api.openai.com/v1"
            model = 'gpt-3.5-turbo'
            st.header('To create your winning proposal')  # Display header

            class ConversationBot:  # Define ConversationBot class for managing chat interactions
                def __init__(self, api_key,
                             base_url=base_url,
                             model=model,
                             system_message="""You are a freelancer expert for create freelancing wining purposal""",
                             max_history=5,
                             token_budget=4096
                             ):
                    self.client = OpenAI(api_key=api_key)  # Initialize OpenAI client
                    self.client.base_url = base_url
                    self.model = model
                    self.system_message = system_message
                    self.conversation_history = [{"role": "system", "content": self.system_message}]
                    self.max_history = max_history
                    self.token_budget = token_budget

                def enforce_history_limit(self):
                    while len(self.conversation_history) > self.max_history:
                        self.conversation_history.pop(1)

                def chat_completion(self, prompt, temperature=0.7, max_tokens=500):
                    self.conversation_history.append({"role": "user", "content": prompt})
                    response = self.client.chat.completions.create(model=self.model,
                                                                   messages=self.conversation_history)
                    ai_response = response.choices[0].message.content
                    self.conversation_history.append({"role": "assistant", "content": ai_response})
                    self.enforce_history_limit()
                    return ai_response

            myself = st.text_input("Bidder Name")  # Input field for bidder name
            skil_set = st.text_input("Your Expertise / Skills Set")  # Input field for skills set
            client_project_description = st.text_area("Client Project Description")  # Text area for client project description

            conv_manager = ConversationBot(api_key=api_key)  # Initialize ConversationBot instance

            if st.button("Submit Proposal"):  # Button to submit proposal
                prompt1 = f"Please write a winning proposal, including myself: {myself} and my skill set {skil_set}, against the given client project description {client_project_description} and you must return the response according to system messages."

                response = conv_manager.chat_completion(prompt1)  # Get response from ConversationBot
                response_placeholder = st.empty()  # Placeholder for response
                response_placeholder.write(f'{response}')  # Display response
                st.session_state.response_content = response  # Store response content in session state

    elif choice == "About Us":  # If user selects "About Us"
        about_us()  # Call about_us function


if __name__ == "__main__":
    main()  # Call the main function when the script is executed directly
