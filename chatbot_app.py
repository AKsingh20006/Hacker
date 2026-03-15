{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO61NSptjSDyxdOFD3LxJjU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AKsingh20006/Hacker/blob/main/chatbot_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JTOKFsiNnZQc",
        "outputId": "b38b9097-64b8-4e61-ba52-f196a8448d30"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.55.0-py3-none-any.whl.metadata (9.8 kB)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<8,>=5.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.2.6)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.3.1)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.46)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (26.0)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<13,>=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.6)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (9.1.4)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.5.1)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.10.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.26.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.17.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.3)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.4.5)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.11)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2026.2.25)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.3)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.0.3)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (25.4.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2025.9.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.37.0)\n",
            "Requirement already satisfied: rpds-py>=0.25.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.30.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
            "Downloading streamlit-1.55.0-py3-none-any.whl (9.1 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.1/9.1 MB\u001b[0m \u001b[31m51.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m79.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.55.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "144b979d",
        "outputId": "67fd19b2-154d-41ad-850d-92008c59e13e"
      },
      "source": [
        "import streamlit as st\n",
        "\n",
        "# Page title\n",
        "st.set_page_config(page_title=\"Student Assistant Chatbot\")\n",
        "\n",
        "st.title(\"🎓 Student Assistant Chatbot\")\n",
        "st.write(\"Ask about exams, assignments, courses, or faculty information.\")\n",
        "\n",
        "# Course dataset\n",
        "courses = {\n",
        "    \"data mining\": {\n",
        "        \"exam\": \"25 March\",\n",
        "        \"assignment\": \"20 March\",\n",
        "        \"faculty\": \"Dr. Sharma\",\n",
        "        \"email\": \"sharma@college.edu\"\n",
        "    },\n",
        "    \"artificial intelligence\": {\n",
        "        \"exam\": \"28 March\",\n",
        "        \"assignment\": \"22 March\",\n",
        "        \"faculty\": \"Dr. Mehta\",\n",
        "        \"email\": \"mehta@college.edu\"\n",
        "    },\n",
        "    \"data structures\": {\n",
        "        \"exam\": \"30 March\",\n",
        "        \"assignment\": \"24 March\",\n",
        "        \"faculty\": \"Dr. Rao\",\n",
        "        \"email\": \"rao@college.edu\"\n",
        "    }\n",
        "}\n",
        "\n",
        "# Initialize chat history\n",
        "if \"messages\" not in st.session_state:\n",
        "    st.session_state.messages = []\n",
        "\n",
        "# Function to generate response\n",
        "def chatbot_response(question):\n",
        "    question = question.lower()\n",
        "\n",
        "    for course in courses:\n",
        "        if course in question:\n",
        "\n",
        "            if \"exam\" in question:\n",
        "                return f\"The {course.title()} exam is on {courses[course]['exam']}.\"\n",
        "\n",
        "            elif \"assignment\" in question:\n",
        "                return f\"The {course.title()} assignment deadline is {courses[course]['assignment']}.\"\n",
        "\n",
        "            elif \"faculty\" in question or \"teacher\" in question:\n",
        "                return f\"The faculty for {course.title()} is {courses[course]['faculty']} ({courses[course]['email']}).\"\n",
        "\n",
        "            else:\n",
        "                return f\"For {course.title()} — Exam: {courses[course]['exam']}, Assignment: {courses[course]['assignment']}, Faculty: {courses[course]['faculty']}.\"\n",
        "\n",
        "    return \"Sorry, I can only help with exam schedules, assignments, courses, and faculty information.\"\n",
        "\n",
        "# Display chat history\n",
        "for message in st.session_state.messages:\n",
        "    with st.chat_message(message[\"role\"]):\n",
        "        st.markdown(message[\"content\"])\n",
        "\n",
        "# User input\n",
        "if prompt := st.chat_input(\"Ask a question\"):\n",
        "    st.session_state.messages.append({\"role\": \"user\", \"content\": prompt})\n",
        "\n",
        "    with st.chat_message(\"user\"):\n",
        "        st.markdown(prompt)\n",
        "\n",
        "    response = chatbot_response(prompt)\n",
        "\n",
        "    with st.chat_message(\"assistant\"):\n",
        "        st.markdown(response)\n",
        "\n",
        "    st.session_state.messages.append({\"role\": \"assistant\", \"content\": response})"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-03-15 10:20:57.101 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.104 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.105 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.106 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.109 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.111 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.112 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.113 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.114 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.115 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.117 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.119 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.122 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.125 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.127 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.128 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-03-15 10:20:57.128 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py"
      ],
      "metadata": {
        "id": "NYjWNlXRqY3w",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "06a2d1d0-c787-4a36-878e-31b809acf94f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.27.160.85:8501\u001b[0m\n",
            "\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "8F5k7PpWBDZi"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}