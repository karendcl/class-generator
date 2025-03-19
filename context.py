def get_context_default():
    role = (
        "Act as a university professor with expertise in teaching programming to non-technical students. "
        "Your task is to design a structured class to teach the programming language Octave to biology "
        "students who have no prior programming experience."
    )

    skills = "The students have already been taught the above lesson"
    objectives = "The objective of the class is to teach ..."

    to_create = """Based on these objectives, create a detailed class plan that includes:
                    0. **Recap**: A brief recap of the previous class.
                    1. **Class Topics**: A list of topics to cover, organized in a logical sequence for beginners.
                    2. **Learning Outcomes**: What students should be able to do after each topic.
                    3. **Teaching Methodology**: How you will teach each topic (e.g., lectures, hands-on exercises, 
                    examples).
                    4. **Data Examples**: Provide real-world biological datasets or examples that will be used to teach 
                    each topic.
                    5. **Specific Instructions**:
                    - Include octave code snippets and explanations.
                    - Break down the class into sections with time estimates. The class should be around 1 hour.

                    Ensure that the class is beginner-friendly, engaging, and tailored to the needs of biology students. 
                    Use simple language and avoid unnecessary technical jargon."""

    return role, skills, objectives, to_create