# 1. Import thư viện các thư viện cần thiết:
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 2. Tải bộ dữ liệu:https://drive.google.com/file/d/1qeJqFtRdjjHqExbWJcgKy0yJbczTTAE3/view

# 3. Đọc bộ dữ liệu:
dataset_path = 'C:/Users/ACER/Desktop/Git/AIO-Exercise/MODULE3/week4/Housing.csv'
df = pd.read_csv(dataset_path)

# 4. Xử lý dữ liệu categorical:
categorical_cols = df.select_dtypes(include=['object']).columns.to_list()
ordinal_encoder = OrdinalEncoder()
encoded_categorical_cols = ordinal_encoder.fit_transform(df[categorical_cols])
encoded_categorical_df = pd.DataFrame(
    encoded_categorical_cols,
    columns=categorical_cols
)
numerical_df = df.drop(categorical_cols, axis=1)
encoded_df = pd.concat(
    [numerical_df, encoded_categorical_df],
    axis=1
)

# 5. Chuẩn hóa bộ dữ liệu:
normalizer = StandardScaler()
dataset_arr = normalizer.fit_transform(encoded_df)

# 6. Tách dữ liệu X, y:
X, y = dataset_arr[:, 1:], dataset_arr[:, 0]

# 7. Chia tập dữ liệu train, val:
test_size = 0.3
random_state = 1
is_shuffle = True

X_train, X_val, y_train, y_val = train_test_split(
    X, y,
    test_size=test_size,
    random_state=random_state,
    shuffle=is_shuffle
)

# 8. Huấn luyện mô hình:
# Huấn luyện mô hình RandomForestRegressor
regressor = RandomForestRegressor(
    random_state=random_state
)
regressor.fit(X_train, y_train)

# Huấn luyện mô hình AdaBoostRegressor

regressor = AdaBoostRegressor(
    random_state=random_state
)
regressor.fit(X_train, y_train)

# Huấn luyện mô hình GradientBoostingRegressor

regressor = GradientBoostingRegressor(
    random_state=random_state
)
regressor.fit(X_train, y_train)

# 9. Đánh giá mô hình:

y_pred = regressor.predict(X_val)

mae = mean_absolute_error(y_val, y_pred)
mse = mean_squared_error(y_val, y_pred)

print('Evaluation results on validation set:')
print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
