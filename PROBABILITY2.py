import random
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)
total_bullets_700 = set()
for bullets in sorted_df_jobs[:700].Bullets:
 total_bullets_700.update([bullet.strip()
 for bullet in bullets])
total_bullets_700 = sorted(total_bullets_700)
vectorizer_700 = TfidfVectorizer(stop_words='english')
tfidf_matrix_700 = vectorizer_700.fit_transform(total_bullets_700)
shrunk_norm_matrix_700 = shrink_matrix(tfidf_matrix_700)

print(f"We've vectorized {shrunk_norm_matrix_700.shape[0]} bullets")
np.random.seed(0)
generate_elbow_plot(shrunk_norm_matrix_700)
plt.show()
