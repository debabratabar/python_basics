import json

def load_data():
    resultList =[]
    try:
        with open('youtube_playlist.txt' , 'r') as file:
            resultList= json.load(file)
            return resultList
    except FileNotFoundError:
        return []


def add_videos(videoList):
    video_name = input("Please Enter video Name =\n")
    duration =input("Please enter video duration:\n") 
    new_video = {'name':video_name , 'duration': duration }
    videoList.append(new_video)

    save_the_data(videoList)



def list_all_videos(videoList):
    print('-' *10 , "Video List " , '-' *10 )
    try:
        # fileinst= open('youtube_playlist.txt' , 'r')
        for (id , videoDetails) in enumerate(videoList, start=1):
            print(f"{id}. Video Name : {videoDetails['name']} , Duration : {videoDetails['duration']}")
    except FileNotFoundError:
        return [] 
    print('-'*40)

def delete_videos(videoList):
    try:
        id = int(input("Enter your video id:\n"))
        videoList.pop(id-1)
    except IndexError:
        print("Invalid Id")
    save_the_data(videoList)

def update_videos(videoList):
    
    id = int(input("Enter your video id:\n"))
    try:
        video_name = input("Please Enter new video Name =\n")
        duration =input("Please enter new video duration:\n") 

        videoList[id-1]['name'] = video_name
        videoList[id-1]['duration'] = duration
    except IndexError:
        print("Invalid Id")
    
    save_the_data(videoList)


def save_the_data(videoList):
    with open('youtube_playlist.txt' , 'w') as file:
        # json.dump(enumerate(videoList , start=1) , file)
        json.dump(videoList , file)


def __main__():
    videoList = load_data()
    while(True):
        print("Welcome to Youtube Manager App")
        print("PLease Choose below option")
        print("1. List of All Videos ")
        print("2. Add new Video ")
        print("3. delete video")
        print("4. Update a video ")
        print("5. Exit from the app ")
        print("Enter your choice :")
        choice = input()


        match choice:
            case '1':
                list_all_videos(videoList)
            case '2':
                add_videos(videoList)
            case '3':
                delete_videos(videoList)
            case '4':
                update_videos(videoList)
            case '5':
                print("Have a Nice Day!!")
                break
            case _:
                print("Please Enter Corect Input , Thanks !! ")





if __name__ == "__main__":
    __main__()