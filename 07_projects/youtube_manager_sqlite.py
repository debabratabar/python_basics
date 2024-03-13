import sqlite3
import json

# creating the connection , cursor & table 
conn = sqlite3.connect("youtube.db")
curser = conn.cursor()
curser.execute("Create table if not exists youtube_mang( id Integer , VideoName String, duration String)")




def list_all_videos():
    print('-' *10 , "Video List " , '-' *10 )
    result = curser.execute("Select * from youtube_mang")
    # print(result.fetchall())
    for item in result.fetchall():
        print(f" {item[0]} VideoName: {item[1]} | Duration : {item[2]}")

    print('-'*40)

def add_videos():
    video_name = input("Please Enter video Name =\n")
    duration =input("Please enter video duration:\n") 
    maxId = curser.execute("select max(id)+1 from youtube_mang").fetchone()[0]
    if maxId == None:
        maxId = 1 
    curser.execute("Insert into  youtube_mang(id , VideoName , duration ) values(?,?,? )",(maxId , video_name , duration))
    conn.commit()

def delete_videos():
    list_all_videos()
    id = int(input("Enter your video id:\n"))
    # checkId = curser.execute("select id from youtube_mang where id = ?" , (id,)).fetchone()[0]
    # print(checkId)
    if curser.execute("select id from youtube_mang where id = ?" , (id,)).fetchone() != None:
        curser.execute("Delete from youtube_mang where id = ? ",(id,))
        conn.commit()
    else:
        print("Invalid Input")

def update_videos():
    list_all_videos()
    id = int(input("Enter your video id:\n"))
    if curser.execute("select id from youtube_mang where id = ?" , (id , )).fetchone() != None:
        video_name = input("Please Enter  new  video Name =\n")
        duration =input("Please enter  new video duration:\n")
        curser.execute("update youtube_mang set VideoName=? , duration=? where id=?", (video_name , duration , id))
        conn.commit()
    else:
        print("Invalid Input")

    


def __main__():
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
                list_all_videos()
            case '2':
                add_videos()
            case '3':
                delete_videos()
            case '4':
                update_videos()
            case '5':
                print("Have a Nice Day!!")
                conn.close()
                break
            case _:
                print("Please Enter Corect Input , Thanks !! ")





if __name__ == "__main__":
    __main__()
