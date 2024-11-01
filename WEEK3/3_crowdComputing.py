from statistics import mean

crowdEsti = [1000,5818,1786,2000,1500,1500,100,120, 150, 150, 158,170,175,100,197,200,200,200,200,200,200, 220,220,220,229,234,258,258,258,250,258,258,250,250,250,263,270,275,275,285,300, 308, 300, 30, 0,300,300,300,300,328,350,358,350,480,408,480,408,400,450,467,500,588,500,500,500,500,500]

crowdEsti.sort();
print(crowdEsti);
print("------------------------")

crowdEsti = crowdEsti[int(0.05*len(crowdEsti)):]
print(crowdEsti);

print("------------------------")
crowdEsti = crowdEsti[: len(crowdEsti)-int(0.05*len(crowdEsti))]
print(crowdEsti);

print(mean(crowdEsti));

# MERTHOD 2
from scipy import stats

crowdEsti = [1000,5818,1786,2000,1500,1500,100,120, 150, 150, 158,170,175,100,197,200,200,200,200,200,200, 220,220,220,229,234,258,258,258,250,258,258,250,250,250,263,270,275,275,285,300, 308, 300, 30, 0,300,300,300,300,328,350,358,350,480,408,480,408,400,450,467,500,588,500,500,500,500,500]

m = stats.trim_mean(crowdEsti, 0.05)
print(m) # 350.42622950819674