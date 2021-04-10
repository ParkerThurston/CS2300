from pytube import YouTube 
  
# where to save 
SAVE_PATH = "D:\College Stuff\Freshman\CS 2300\CS2300" #to_do 
  
# link of the video to be downloaded 
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
  
try: 
    # object creation using YouTube
    # which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception 
  
# filters out all the files with "mp4" extension 

mp4files = yt.filter('mp4') 
  
#to set the name of the file
yt.set_filename('GeeksforGeeks Video')  
  
# get the video with the extension and
# resolution passed in the get() function 
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
try: 
    # downloading the video 
    d_video.download(SAVE_PATH) 
except: 
    print("Some Error!") 
print('Task Completed!') 





# class BookRecsGui(EasyFrame):
#     def __init__(self):
#         EasyFrame.__init__(self, title = "Book Recommendations", 
#                                 width = 220, 
#                                 height= 100, 
#                                 background="powder blue",
#                                 resizable= True)

    #     self.btnFriends = self.addButton(text="Friends", row = 0, column = 0, command = self.getFriends)
    #     self.btnRecomm = self.addButton(text="Recommend", row = 0, column = 1, command = self.recommendations)
    #     self.btnReport = self.addButton(text="Report", row = 0, column = 2, command = self.Report)


    # def getFriends(self):
    #     name = self.prompterBox("Friends", "Enter Reader Name:")
    #     if name in BookSuggestionParkerThurston.ratings.keys():
    #         friends = BookSuggestionParkerThurston.friends(name)
    #         self.messageBox("Friends of " + name, friends[0] +'\n'+friends[1])
    #     else:
    #         self.messageBox("Error", "No such reader.")
        

    # def recommendations(self):
    #     name = self.prompterBox("Recommendations", "Enter Reader Name:")
    #     if name in BookSuggestionParkerThurston.ratings.keys():
    #         top2 = BookSuggestionParkerThurston.friends(name)
    #         recommends = BookSuggestionParkerThurston.recommend(name,top2)
    #         brStr = ""
    #         for book in recommends:
    #             brStr += book[0] +", " + book[1] +"\n"
    #         self.messageBox("Recommendations for " + name, brStr, width = 100, height= 50)
    #     else:
    #        self.messageBox("Error", "No such reader.") 
    # def Report(self):
        
    #     self.messageBox("Report", BookSuggestionParkerThurston.report(), width = 100, height= 50)
    
    

# def main():
#     Downloadvid()

# if __name__ == "__main__":
#     main()

