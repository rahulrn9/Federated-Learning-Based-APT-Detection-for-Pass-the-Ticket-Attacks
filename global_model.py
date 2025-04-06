from sklearn.ensemble import RandomForestClassifier
import joblib

class GlobalModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def train(self, X, y):
        """Train the model with features X and labels y."""
        self.model.fit(X, y)

    def predict(self, X):
        """Predict labels for unseen data."""
        return self.model.predict(X)

    def save(self, path='models/global_model.pkl'):
        """Save the trained model to a file."""
        joblib.dump(self.model, path)

    def load(self, path='models/global_model.pkl'):
        """Load a trained model from a file."""
        self.model = joblib.load(path)
