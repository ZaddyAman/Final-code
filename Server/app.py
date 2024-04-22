from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from flask import Flask, request, render_template
import pandas as pd 
from typing import Any



import joblib

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib



# Load the trained models (replace with your actual file paths)

    





app = Flask(__name__)
CORS(app)

model_albumin: Any = joblib.load('Server/pickel_fiels/model_albumin.pkl')
model_alanine:Any = joblib.load("Server/pickel_fiels/model_alanine.pkl")
model_ast:Any =joblib.load("Server\pickel_fiels\model_ast.pkl")
model_phosphotase:Any =joblib.load("Server\pickel_fiels\model_phosphotase.pkl")
model_nitrogen:Any =joblib.load("Server\pickel_fiels\model_nitrogen.pkl")
model_calcium:Any =joblib.load("Server\pickel_fiels\model_calcium.pkl")
model_cholesterol:Any =joblib.load("Server\pickel_fiels\model_cholesterol.pkl")
model_bicarbonate:Any =joblib.load("Server\pickel_fiels\model_bicarbonate.pkl")
model_iron:Any =joblib.load("Server\pickel_fiels\model_iron.pkl")
model_phosphorus:Any =joblib.load("Server\pickel_fiels\model_phosphorus.pkl")
model_bilirubin:Any =joblib.load("Server\pickel_fiels\model_bilirubin.pkl")
model_protein:Any =joblib.load("Server\pickel_fiels\model_protein.pkl")
model_Creatinine:Any =joblib.load("Server\pickel_fiels\model_Creatinine.pkl")
model_sodium:Any =joblib.load("Server\pickel_fiels\model_sodium.pkl")
model_pottasium:Any =joblib.load("Server\pickel_fiels\model_pottasium.pkl")
model_chloride:Any =joblib.load("Server\pickel_fiels\model_chloride.pkl")
model_globulin:Any =joblib.load("Server\pickel_fiels\model_globulin.pkl")
model_glucose: Any =joblib.load("Server\pickel_fiels\model_glucose.pkl")


@app.route("/submit", methods=["POST"])
def predict():
    
    male_ranges={
        "albumin": {"medication_low": 2.4, "medication_high": 6},
        "  alanine": {"medication_low": 7, "medication_high":67},
        "ast": {"medication_low": 7, "medication_high": 48},
        "phosphotase": {"medication_low": 31, "medication_high": 176},
        " nitrogen": {"medication_low": 5.6, "medication_high": 30},
        "calcium": {"medication_low": 1.6, "medication_high": 3.2},
        "cholesterol": {"medication_low": 28, "medication_high": 150},
        "bicarbonate": {"medication_low": 15.4, "medication_high": 36},
        "iron": {"medication_low": 49, "medication_high": 210},
        "phosphorus": {"medication_low": 1.96, "medication_high": 5.4},
        "bilirubin ": {"medication_low": 0.21, "medication_high": 1.3},
        "protein": {"medication_low": 4.2, "medication_high": 10},
        "Creatinine": {"medication_low": 0.42, "medication_high": 1.45},
        "sodium": {"medication_low": 94.5, "medication_high": 174},
        "pottasium": {"medication_low": 2.45, "medication_high": 6},
        "chloride": {"medication_low": 67.2, "medication_high": 127},
        "globulin": {"medication_low": 1.61, "medication_high": 4.2},
        "glucose": {"medication_low":54 , "medication_high": 141},
    }
    
    female_ranges={
        "albumin": {"medication_low": 2.4, "medication_high": 6},
        "  alanine": {"medication_low": 5, "medication_high": 36},
        "ast": {"medication_low": 6.3, "medication_high": 30},
        "phosphotase": {"medication_low": 31, "medication_high": 176.4},
        " nitrogen": {"medication_low": 4.2, "medication_high": 25.2},
        "calcium": {"medication_low": 1.6, "medication_high": 3.12},
        "cholesterol": {"medication_low": 28, "medication_high": 120},
        "bicarbonate": {"medication_low": 15.4, "medication_high": 34.8},
        "iron": {"medication_low": 35, "medication_high": 204},
        "phosphorus": {"medication_low": 1.9, "medication_high": 5.4},
        "bilirubin ": {"medication_low": 0.21, "medication_high": 1.2},
        "protein": {"medication_low": 4.2, "medication_high": 9.96},
        "Creatinine": {"medication_low": 0.35, "medication_high": 1.32},
        "sodium": {"medication_low": 94.5, "medication_high": 174},
        "pottasium": {"medication_low": 2.45, "medication_high": 6},
        "chloride": {"medication_low": 67.2, "medication_high": 127.2},
        "globulin ": {"medication_low": 1.4, "medication_high": 3.84},
        "glucose": {"medication_low": 54, "medication_high": 140.4},
        
    }
    
    models = [
        model_albumin, model_alanine, model_ast, model_phosphotase, model_nitrogen,
        model_calcium, model_cholesterol, model_bicarbonate, model_iron, model_phosphorus,
        model_bilirubin, model_protein, model_Creatinine, model_sodium, model_pottasium,
        model_chloride, model_globulin, model_glucose
    ]
    
    attributes = [
        'albumin', '  alanine', 'ast', 'phosphotase', ' nitrogen', 'calcium', 'cholesterol',
        'bicarbonate', 'iron', 'phosphorus', 'bilirubin ', 'protein', 'Creatinine ', 'sodium',
        'pottasium', 'chloride', 'globulin', 'glucose'
    ]

    diet_recommendations = {
        'albumin': {
            'Excess': {
                'veg': ['Cucumbers','Carrots','Radishes', 'Garlic'],
                'non-veg': ['sirloin','tenderloin','Fish','fillets'],
                'fruits': ['Starfruit', 'Acerola (Barbados Cherry)','Sapodilla (Chikoo)'],
                
            },
            'Deficiency': {
                'veg': ['Spinach','Brussels','Sprouts','Broccoli'],
                'non-veg': ['egg whites','Skinless','boneless chicken breast'],
                'fruits': ['Guava','Longan','Indian Blackberry (Jamun)'],
            }
        },
        '  alanine': {
            'Excess': {
                'veg': ['Turmeric','Ginger','Garlic','Onions'],
                'non-veg': ['Rainbow trout','cod fish', 'haddock fish'],																						             
                'fruits': ['Boysenberry','Tindora (Ivy Gourd)'],
            },
            'Deficiency': {
                'veg': ['Collard Greens','Mustard Greens','Swiss Chard'],
                'non-veg': ['egg yolks','pork' ,'beef'],
                'fruits': ['Jabuticaba','Custard Apple (Sitaphal)'],
            }
        },
        
        'ast':{
            'Excess': {
                'veg': ['Bitter Melon (Karela)','Turmeric','Onions', 'ginger'],
                'non-veg': ['Catfish','squid'],
                'fruits': ['Papaya','Indian Plums(Ber)'],
            },
            'Deficiency': {
                'veg': ['Spinach','Collard Greens','Kale','Swiss Chard'],
                'non-veg': ['salmon fish', 'mackerel fish','mullet fish'],
                'fruits': ['Boysenberry','Ridge Gourd (Turai)'],
            }
            
        },
        'phosphotase': {
            'Excess': {
                'veg': ['Okra','Collards'],
                'non-veg': ['Salmon fish','Tuna fish'],
                'fruits': ['Apple, Peaches'],
            },
            'Deficiency': {
                'veg': ['Brocolli','Spinach'],
                'non-veg': ['Lean meat','Fish','Eggs'],
                'fruits': ['Oranges','Bananas','Berries'],
            }
        },
        ' nitrogen': {
            'Excess': {
                'veg': ['Cucumber','Watermelon','Celery', 'Lettuce'],
                'non-veg': ['Rainbow trout','Squid'],
                'fruits': ['Papaya','Feijoa','Guanabana (Graviola)'],
            },
            'Deficiency': {
                'veg': ['Green peas','Spinach','Cabbage','Beet Greens'],
                'non-veg': ['Lamb meat','Salmon roe'],
                'fruits': ['Watermelon','Sapodilla','Jujube'],
            }
        },
        'calcium': {
            'Excess': {
                'veg': ['Kale','Swiss Chard','Spinach','Beet Greens', 'Mustard Greens'],
                'non-veg': ['Lean Cuts of Red Meat','Skinless Poultry','haddock fish', 'flounder fish'],
                'fruits': ['Figs','Jackfruit'],
            },
            'Deficiency': {
                'veg': ['Bok Choy','Mustard Greens','Turnip Greens','Okra'],
                'non-veg': ['Canned Fish with Bones','Bone Broth','Prawns with Shell','Soft Shell Crab'],
                'fruits': ['Jackfruit','Tamarind'],
            }
        },
        'cholesterol': {
            'Excess': {
                'veg': ['Okra','Bitter Melon (Karela)','Eggplant (Brinjal)','Fenugreek Leaves (Methi)'],
                'non-veg': ['herring fish','cod fish','skinless chicken'],
                'fruits': ['Kiwi', 'Dragon Fruit','Mulberry', 'Horned Melon','Starfruit','Boysenberry','Black Currant','Cranberry'],
            },
            'Deficiency': {
                'veg': ['Spinach','Beet Greens','Kale,Collard Greens','Swiss Chard'],
                'non-veg': ['salmon fish','mackerel fish''sardines fish', 'shrimps','Oysters'],
                'fruits': ['Acai Berry', 'Muscadine Grape','Acerola (Barbados Cherry)','Mamey Sapote' ,'Loquat','Kumquat'],
            }
        },
        'bicarbonate': {
            'Excess': {
                'veg': ['cauliflower','eggplant'],
                'non-veg': ['(Avoid non-veg)'],
                'fruits': ['Raisins','peaches,pears'],
            },
            'Deficiency': {
                'veg': ['Spinach','Kale'],
                'non-veg': ['Chicken','Turkey'],
                'fruits': ['Lemon','Apple','Berries'],
            }
        },
        'iron': {
            'Excess': {
                'veg': ['Onions','Spinach'],
                'non-veg': ['Eggs'],
                'fruits': ['plums','sweet cheeries'],
            },
            'Deficiency': {
                'veg': ['Lentils','Brocolli'],
                'non-veg': ['Red meat','Fish'],
                'fruits': ['Apricots','Watermelon'],
            }
        },
        'phosphorus': {
            'Excess': {
                'veg': ['Cucumber','cabbage'],
                'non-veg': ['tenderloin','bison steaks'],
                'fruits': ['Cranberry','Lemon'],
            },
            'Deficiency': {
                'veg': ['Potatoes','Peas'],
                'non-veg': ['Eggs','Fish'],
                'fruits': ['Grapes','Bananas'],
            }
        },
        'bilirubin ': {
            'Excess': {
                'veg': ['Bitter Gourd (Karela)', 'Barley Grass','Okra (Ladyfinger)','Papaya Leaves'],
                'non-veg': ['shrimp','scallops','cod fish', 'haddock fish'],
                'fruits': ['Tamarind','Sapodilla','Bael Fruit (Wood Apple)'],
            },
            'Deficiency': {
                'veg': ['Collard Greens','Spinach','Beet Greens','Kale'],
                'non-veg': ['pork liver','Egg yolks','Salmon Fish'],
                'fruits': ['Watermelon','Blackberry','Kokum', 'Indian Fig (Anjeer)'],
            }
        },
        'protein': {
            'Excess': {
                'veg': ['Peppers','Tomatoes'],
                'non-veg': ['(Avoid non-veg'],
                'fruits': ['Peaches','Apples'],
            },
            'Deficiency': {
                'veg': ['Quinoa','Spinach'],
                'non-veg': ['Fish','lean Meat'],
                'fruits': ['Avocado','Bananas'],
            }
        },
        'Creatinine ': {
            'Excess': {
                'veg': ['Celery','cucumber','Cabbage'],
                'non-veg': ['chicken thighs','catfish'],
                'fruits': ['Durian','Guava','Horned Melon (Kiwano)'],
            },
            'Deficiency': {
                'veg': ['Fenugreek Leaves (Methi)','Bottle Gourd (Lauki)'],
                'non-veg': ['Beef jerky','Venison'],
                'fruits': ['Starfruit','Tamarind','Jackfruit'],
            }
        },
        'sodium': {
            'Excess': {
                'veg': ['Kale','Swiss Chard','Collard Greens','Brussels,,Sprouts'],
                'non-veg': ['Chicken','turkey','beef','porksea bass','tuna fish'],
                'fruits': [' Amla (Indian Gooseberry)','Dragon Fruit','Horned Melon'],
            },
            'Deficiency': {
                'veg': ['Beetroot','Carrots','Spinach','Sweet Potatoes','Pumpkin'],
                'non-veg': ['Ham meet','chicken'],
                'fruits': ['Cranberry','Mulberry'],
            }
        },
        'pottasium': {
            'Excess': {
                'veg': ['Broccoli','Zucchini','Green Beans','Cauliflower'],
                'non-veg': ['boneless chicken breast','Lean pork','Shrimp'],
                'fruits': ['Pomegranate','Dragon Fruit'],
            },
            'Deficiency': {
                'veg': ['Sweet Potatoes','Beetroot','Spinach','Swiss Chard'],
                'non-veg': ['Lean Beef','Tuna fish, Salmon Fish'],
                'fruits': ['Banana','Guava'],
            }
        },
        'chloride': {
            'Excess': {
                'veg': ['Zucchini','Cucumber'],
                'non-veg': ['Cod Fish, egg(without salt)'],
                'fruits': ['Apple','Strawberry',],
            },
            'Deficiency': {
                'veg': ['Celery','Tomatoes'],
                'non-veg': ['Saltwater fish','Chicken'],
                'fruits': ['Pineapple','Watermelon'],
            }
        },
        'globulin ': {
            'Excess': {
                'veg': ['kale','cauliflower','cucumber'],
                'non-veg': ['codfish','tofu','turkey breasts'],
                'fruits': ['berries','apple','grapefruit'],
            },
            'Deficiency': {
                'veg': ['Spinach','brocolli','bell peppers'],
                'non-veg': ['chicken','salmon fish','eggs'],
                'fruits': ['Banana','orange','avocado'],
            }
        },
        'glucose': {
            'Excess': {
                'veg': ['Bitter Melon (Karela)','Fenugreek Leaves(Methi)','Okra (Ladyfinger)'],
                'non-veg': ['salmon fish','mackerel fish', 'sardines fish crab'],
                'fruits': ['Cactus Pear (Prickly Pear)','Loquat', 'Dragon Fruit'],
            },
            'Deficiency': {
                'veg': [' sweet potatoes','beets','carrots'],
                'non-veg': ['lean meats','fish','eggs'],
                'fruits': ['bananas','grapes','mangoes'],
            }
        }     
        
    }
    
    
    
    try:
        # Get data from the request body
        data = request.get_json()
        gender = data['gender']
        
        if gender == 1:
            gen="male"
        else:
            gen="female"
        
            
        attributes_val = data['attributes']
        out = attributes_val + [gender]

        # Prepare input data for predictions using the attributes array
        input_data = []
        medication_attributes = []  # To store attributes needing medication

        for i, model in enumerate(models):
            if out[i] != -1:
                if gen == "male":
                    low_range = male_ranges[attributes[i]]['medication_low']
                    high_range = male_ranges[attributes[i]]['medication_high']
                elif gen == "female":
                    low_range = female_ranges[attributes[i]]['medication_low']
                    high_range = female_ranges[attributes[i]]['medication_high']

                if (low_range is not None and float(out[i]) <= low_range) or \
                       (high_range is not None and float(out[i]) >= high_range):

                    medication_attributes.append(attributes[i])
                    input_data.append("Medication required")
                else:
                    input_dataframe = pd.DataFrame([[out[i], out[18]]], columns=[attributes[i], 'gender'])
                    prediction = model.predict(input_dataframe)[0]
                    input_data.append(prediction)
            else:
                input_data.append("No prediction for " + attributes[i])
        print(input_data)        

        # Get diet recommendations based on predictions
        diet_results = []
        for i, pred in enumerate(input_data):
            if attributes[i] in medication_attributes:
                diet_results.append({'attribute': attributes[i], 'recommendations': "Medication required"})
            elif pred == "No prediction for " + attributes[i]:
                diet_results.append({'attribute': attributes[i], 'recommendations': "No input provided"})
            else:
                attribute = attributes[i]
                attribute_diet = diet_recommendations.get(attribute, {}).get(pred, {})
                diet_results.append({'attribute': attribute, 'recommendations': attribute_diet})

        # Return response with predictions and diet recommendations
        print(diet_results)
        return jsonify({"diet_recommendations": diet_results})

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "An error occurred during processing."}), 500

if __name__ == "__main__":
    app.run(debug=True)
