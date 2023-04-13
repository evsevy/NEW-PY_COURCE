from pyecharts import Bar
Bar = Bar("Months Vs Sales of Car", "Various Manufactures")
Bar.add("Mahindra", ['MAY','JUNE','JUL','AUG'], [45,38,20,50], IS_MORE_UTILS = True)
Bar.add("Tata", ['MAY','JUNE','JUL','AUG'], [40,48,38,50], IS_MORE_UTILS = True)
Bar.add("Kia", ['MAY','JUNE','JUL','AUG'], [50,42,15,20], IS_MORE_UTILS = True)
Bar.render('bar.html') # Generates a Bar.html file in the specified directory

from pyecharts import Line
attr =["Shirt", "T-Shirt", "Jeans", "Kurtas", "Salvar", "Shoes"]
v1 =[5, 20, 36, 10, 10, 100]
v2 =[55, 60, 16, 20, 15, 80]
line =Line("Pacing chart for Shop A and Shop B","X-axis-->Cloths, Y-axis-->Pricing")
line.add("Shop A", attr, v1, mark_point=["average"])
line.add("Shop B", attr, v2, is_smooth=True, mark_line=["max", "average"])
line.render('poly_line.html')


from pyecharts import Gauge
gauge = Gauge('project completion progress')
gauge.add('progress table', 'completion rate' , 73.28)
gauge.render('Gauge.html')
