import google.generativeai as genai

genai.configure(api_key="AIzaSyD-kvw8w7yUMRhC_jCUwy5ccff3lUlVR7k")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content('pergunta')
print(response.text)


