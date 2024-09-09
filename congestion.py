import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the modified dataset
file_path = 'modified_weather_traffic_data.csv'
df = pd.read_csv(file_path)

# Preprocessing
# Convert categorical variables to numeric using LabelEncoder
label_encoders = {}
for column in ['weather_condition', 'day_of_week', 'road_type', 'location', 'congestion_level']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Feature-target split
X = df.drop(columns=['congestion_level', 'timestamp', 'location_latitude', 'location_longitude'])
y = df['congestion_level']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=label_encoders['congestion_level'].classes_)

print("Accuracy:", accuracy)
print("Classification Report:\n", report)
