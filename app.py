import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# ---------------------------------------------------
# Streamlit UI Setup
# ---------------------------------------------------
st.set_page_config(
    page_title="Text To Math Problem Solver And Data Search Assistant",
    page_icon="🧮"
)

st.title("Text To Math Problem Solver Using Google Gemma 2")

groq_api_key = st.sidebar.text_input("Groq API Key", type="password")

if not groq_api_key:
    st.info("Please add your Groq API key to continue")
    st.stop()

# ---------------------------------------------------
# Initialize LLM
# ---------------------------------------------------
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=groq_api_key
)

# ---------------------------------------------------
# Modern Wikipedia Tool
# ---------------------------------------------------
wiki_tool = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper()
)

# ---------------------------------------------------
# Math Solver Chain (LCEL)
# ---------------------------------------------------
math_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert mathematician. Solve problems step-by-step with reasoning."),
    ("user", "{question}")
])

math_chain = math_prompt | llm | StrOutputParser()

# ---------------------------------------------------
# Chat History
# ---------------------------------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a Math chatbot who can solve your math questions!"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# ---------------------------------------------------
# User Input
# ---------------------------------------------------
question = st.text_area(
    "Enter your question:",
    "I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. "
    "Then I buy a dozen apples and 2 packs of blueberries. Each pack has 25 berries. "
    "How many total pieces of fruit do I have?"
)

option = st.radio("Choose Mode:", ["Math Solver", "Wikipedia Search"])

# ---------------------------------------------------
# Run Button
# ---------------------------------------------------
if st.button("Find My Answer"):
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        st.chat_message("user").write(question)

        with st.spinner("Generating response..."):
            if option == "Math Solver":
                response = math_chain.invoke({"question": question})

            elif option == "Wikipedia Search":
                response = wiki_tool.run(question)

            st.session_state.messages.append({"role": "assistant", "content": response})

            st.write("### Response:")
            st.success(response)
    else:
        st.warning("Please enter a question.")
