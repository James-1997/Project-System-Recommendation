from math import sqrt

users = {
          "Angelica":
                      {
                      "Blues Traveler": 3.5, "Broken Bells": 2.0,
                      "Norah Jones": 4.5, "Phoenix": 5.0,"Slightly Stoopid": 1.5,"The Strokes": 2.5, "Vampire Weekend": 2.0
                      },

          "Bill":
                      {
                        "Blues Traveler": 2.0, "Broken Bells": 3.5,"Deadmau5": 4.0, "Phoenix": 2.0,
                        "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0
                      },

          "Chan":
                      {
                        "Blues Traveler": 5.0, "Broken Bells": 1.0,
                        "Deadmau5": 1.0, "Norah Jones": 3.0,
                        "Phoenix": 5, "Slightly Stoopid": 1.0
                      },

          "Dan":
                      {
                        "Blues Traveler": 3.0, "Broken Bells": 4.0,
                        "Deadmau5": 4.5, "Phoenix": 3.0,
                        "Slightly Stoopid": 4.5, "The Strokes": 4.0,
                        "Vampire Weekend": 2.0
                      },

          "Hailey":
                      {
                        "Broken Bells": 4.0, "Deadmau5": 1.0,
                        "Norah Jones": 4.0, "The Strokes": 4.0,
                        "Vampire Weekend": 1.0
                      },

          "Jordyn":
                      {
                        "Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0,
                        "Phoenix": 5.0, "Slightly Stoopid": 4.5,
                        "The Strokes": 4.0, "Vampire Weekend": 4.0
                      },

          "Sam":
                      {
                        "Blues Traveler": 5.0, "Broken Bells": 2.0,
                        "Norah Jones": 3.0, "Phoenix": 5.0,
                        "Slightly Stoopid": 4.0, "The Strokes": 5.0
                      },

          "Veronica":
                      {
                        "Blues Traveler": 3.0, "Norah Jones": 5.0,
                        "Phoenix": 4.0, "Slightly Stoopid": 2.5,
                        "The Strokes": 3.0
                      }

          }

######################################################################################################################################################################

print ("Filmes de Veronica: ", users["Veronica"])

######################################################################################################################################################################

def manhattan(rating1,rating2):
  ans=0
  for key in rating1:
    if key in rating2:
      ans+=abs(rating1[key]-rating2[key])
  return ans

######################################################################################################################################################################
  
def minkowski(rating1,rating2,r):
	ans=0;commonRatings=False
	for key in rating1:
		if key in rating2:
			ans+=pow(abs(rating1[key]-rating2[key]),r)
			commonRatings=True
	if commonRatings:
		return pow(ans,1.0/r)
	else:
		return 0
		
######################################################################################################################################################################	

print ("Manhattan Hailey com Veronica: ", manhattan(users['Hailey'], users['Veronica']))
print ("Manhattan Hailey com Jordyn: ",manhattan(users['Hailey'], users['Jordyn']))

######################################################################################################################################################################

def computeNearestNeighbor(username,users):
  distances=[]
  for user in users:
    if user!=username:
      d=minkowski(users[user],users[username],1) #manhattan(users[user],users[username]) 
      distances.append((d,user))
  distances.sort()
  return distances

######################################################################################################################################################################

print ("Nearest Neighbor com Hailey: ", computeNearestNeighbor("Hailey", users))

######################################################################################################################################################################

def recommend(username,users):
	nearest=computeNearestNeighbor(username,users)[0][1]
	reco=[]
	nratings=users[nearest]
	uratings=users[username]
	for band in nratings:
		if band not in uratings:
			reco.append((band,nratings[band]))
	return sorted(reco,key= lambda x:x[1],reverse=True)

######################################################################################################################################################################

print ("recomendando para Hailey: ",recommend('Hailey', users))

######################################################################################################################################################################

def pearson(user1,user2):
	fi=0;se=0;th=0;fo=0;fif=0;co=0
	for band in user1:
		if band in user2:
			print ( "pearson : ", band,user1[band],user2[band] )
			co+=1
			fi+=(user1[band]*user2[band])
			se+=user1[band]
			th+=user2[band]
			fo+=user1[band]**2
			fif+=user2[band]**2
	deno=sqrt(fo-(se**2)/co)*sqrt(fif-(th**2)/co)
	if deno!=0:
		return (fi-(se*th*1.0)/(co*1.0))/deno
	else:
		return 0

######################################################################################################################################################################

print ("r-1", pearson(users['Angelica'], users['Bill']))
print ("r-2", pearson(users['Angelica'], users['Hailey']))
print ("r-3", pearson(users['Angelica'], users['Jordyn']))

######################################################################################################################################################################
