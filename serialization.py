import pickle 

# Methods in the pickle module help to automatically serialize data
# turning it into its hex equivalent (there are other data formats as well) 
# and has methods to deserialize it

print("\n") 


simple_cereal = {"Cornflakes": "Sucks without bananas", "Strawberry Special K": "Super good", "Raisin Bran": "ehhh"}


serialized_cereal = pickle.dumps(simple_cereal)

print(serialized_cereal)


# Bring it back to life from serialization -- can be dangerous if accepting arbitrary user input 
# can open yourself to code injection attacks because the pickle module is vulnerable

deserialized_cereal = pickle.loads(serialized_cereal)

print(" ") 

print(deserialized_cereal)

