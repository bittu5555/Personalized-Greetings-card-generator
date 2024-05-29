import gradio as gr
import pandas as pd

def extract_info_from_excel(primary_key):
    try:
        # Provide the Excel file name
        excel_file_path = "P:\EmployeeDatabase.xlsx"

        # Read Excel file into a DataFrame
        df = pd.read_excel(excel_file_path)

        # Check if the primary key exists in the DataFrame
        if primary_key in df['NGS'].values:
            # Extract data based on the primary key
            selected_data = df[df['NGS'] == primary_key].squeeze()

            # Generate the output prompt
            output_prompt = (
                f"Generate a greetings card for a person who likes {selected_data['SEASON']}, "
                f"{selected_data['TRAVEL'] }," 
                f"{selected_data['COLOUR']} colour,"
                f"{selected_data['FOOD']} food," 
                f"{selected_data['FLOWER']} flower, "
                f"listens to {selected_data['MUSIC']} music, "
                f"and likes to do {selected_data['ACTIVITY']}."
            )

            return output_prompt
        else:
            return f"No data found for ID {primary_key}"
    except Exception as e:
        return f"Error: {str(e)}"

# Create a Gradio interface
iface = gr.Interface(
    fn=extract_info_from_excel,
    inputs=["number"],  # Employee ID as number
    outputs="text",
    live=True,
    title="Employee Information Extractor",
    description="Enter Employee ID to extract information."
)

# Launch the Gradio interface
iface.launch()