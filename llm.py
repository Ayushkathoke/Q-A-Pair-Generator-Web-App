from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate


MODEL_NAME = "llama3.2:latest"
# MODEL_NAME = "llama3.2:1b"
# MODEL_NAME = "qwen:0.5b"


class ChatLL:

    def __init__(self):
        self.llm = OllamaLLM(model=MODEL_NAME)
        self.PROMPT = """
            You are a question generation assistant. Your task is to create {num_questions} high-quality questions based on the provided context. Follow these instructions carefully:

            1. **Question Type**: Generate questions of type "{question_type}".
            2. **Difficulty Level**: Ensure the questions match a "{difficulty_level}" level audience.
            3. **Clarity**: Ensure all questions are clear, accurate, and suitable for the selected type.

            ### Context:
            {context}

            ### Guidelines by Question Type:
            - **Descriptive**: Ask open-ended questions that require detailed written answers.
            - **One-Short**: Create concise questions that expect short and direct answers.
            - **MCQ**: Provide 4 answer options, including one correct answer and 3 plausible distractors.
            - **True/False**: Ask clear factual questions where the answer is either "True" or "False."
            - **Yes/No**: Create straightforward questions answerable with a "Yes" or "No."
            - **Fill in the Blanks**: Write a sentence with one key part missing and provide the correct answer.

            ### Output Format:
            1. **Question Type**: {question_type}
            2. **Question**: [Insert Question Text]
            3. [Optional] Answer Options (for MCQ/Fill in the Blanks):
                - A: [Option 1]
                - B: [Option 2]
                - C: [Option 3]
                - D: [Option 4]
            4. **Correct Answer**: [Insert Correct Answer]
            5. **Explanation**: [Provide a brief explanation if applicable]

            ---

            ### Example Outputs:

            #### **Descriptive**:
            - **Question**: Explain the process of photosynthesis and its importance to life on Earth.
            - **Correct Answer**: Open-ended (Requires detailed explanation).

            #### **One-Short**:
            - **Question**: What is the primary pigment used in photosynthesis?
            - **Correct Answer**: Chlorophyll.

            #### **MCQ**:
            - **Question**: What is the gas released during photosynthesis?
            - A: Oxygen
            - B: Nitrogen
            - C: Carbon Dioxide
            - D: Methane
            - **Correct Answer**: A.

            #### **True/False**:
            - **Question**: Photosynthesis occurs in the mitochondria of plant cells.
            - **Correct Answer**: False.

            #### **Yes/No**:
            - **Question**: Do plants need sunlight for photosynthesis?
            - **Correct Answer**: Yes.

            #### **Fill in the Blanks**:
            - **Question**: Photosynthesis takes place in the _______ of plant cells.
            - A: Nucleus
            - B: Mitochondria
            - C: Chloroplast
            - D: Ribosome
            - **Correct Answer**: C (Chloroplast).

            ---

            Now generate {num_questions} questions based on the context provided, following the structure for the specified question type: "{question_type}".

        """

    def runner(self, numQuestion: int, questionType: str, difficultyLevel: str, context: str) -> str:
        prompt = PromptTemplate(input_types={
            "num_questions": str,
            "question_type": str,
            "difficulty_level": str,
            "context": str
        }, template=self.PROMPT)
        chain = prompt | self.llm
        return chain.invoke({
            "num_questions": numQuestion,
            "question_type": questionType,
            "difficulty_level": difficultyLevel,
            "context": context
        })



    