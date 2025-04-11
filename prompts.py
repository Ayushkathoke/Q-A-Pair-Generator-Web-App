MCQ_PROMPT = """
Generate {num_questions} multiple-choice questions at a {difficulty_level} difficulty level based on the following text:
    - Each question should have a clear, concise question prompt.
    - Provide 4 distinct answer choices (A, B, C, D), one of which is the correct answer.
    - Ensure there is only one correct answer and that the other options are plausible but incorrect.
    - For an 'Easy' difficulty level, ask for basic facts or definitions.
    - For a 'Moderate' difficulty level, ask for concepts and their interconnections.
    - For a 'Hard' difficulty level, include questions that require analysis or synthesis of information.
    - Format: Question: [The Question]  Options: A) [Choice A] B) [Choice B] C) [Choice C] D) [Choice D] Correct Answer: [Letter]
    Text: {text}
"""

TF_PROMPT = """
Generate {num_questions} true/false questions at a {difficulty_level} difficulty level based on the following text:
    - Each question should be a statement that can be evaluated as either true or false.
    - For 'Easy' questions, statements should be straightforward facts or direct interpretations.
    - For 'Moderate' difficulty, statements should test deeper comprehension or implications.
    - For 'Hard' difficulty, statements should require critical thinking or nuanced understanding of the text.
    - Format: Statement: [The Statement] Answer: [True/False]
    Text: {text}
"""

DESCRIPTIVE_PROMPT = """
Generate {num_questions} descriptive questions at a {difficulty_level} difficulty level based on the following text:
    - Each question should encourage a detailed and well-explained answer.
    - For 'Easy' questions, ask for simple explanations or definitions.
    - For 'Moderate' difficulty, ask for elaboration, comparisons, or examples.
    - For 'Hard' difficulty, require critical thinking, synthesis of information, or application of the knowledge in new contexts.
    - Format: Question: [The Question]
    Text: {text}
"""

ONE_SHORT_PROMPT = """
 Generate {num_questions} one-short answer questions at a {difficulty_level} difficulty level based on the following text:
    - Each question should require a concise, direct answer (a few words to a sentence).
    - For 'Easy' questions, ask for basic factual details or clear definitions.
    - For 'Moderate' difficulty, ask for more specific details or examples from the text.
    - For 'Hard' difficulty, ask for answers that require deeper insight, comparison, or elaboration.
    - Format: Question: [The Question] Answer: [The Answer]
    Text: {text}
"""


YN_PROMPT = """
 Generate {num_questions} yes/no questions at a {difficulty_level} difficulty level based on the following text:
    - Each question should require a yes or no response.
    - For 'Easy' questions, provide clear statements with obvious answers.
    - For 'Moderate' difficulty, provide more complex statements that require a better understanding of the material.
    - For 'Hard' difficulty, the statements should be more nuanced, requiring deeper analysis or critical evaluation.
    - Format: Question: [The Question] Answer: [Yes/No]
    Text: {text}
"""

FILL_I_T_B_PROMPT = """
Generate {num_questions} fill-in-the-blank questions at a {difficulty_level} difficulty level based on the following text:
    - Each question should present a sentence or statement with one or more blanks for the user to fill in.
    - For 'Easy' difficulty, the blanks should be filled with key terms or definitions directly mentioned in the text.
    - For 'Moderate' difficulty, the blanks should be filled with terms that require understanding the relationship between concepts.
    - For 'Hard' difficulty, the blanks should require more complex terms or ideas that demand analysis or inference.
    - Format: Statement: [Sentence with a blank] Blank: [The answer]
    Text: {text}
"""