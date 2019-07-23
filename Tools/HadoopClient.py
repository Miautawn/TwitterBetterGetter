from Tools import TwitterCredentials
from hdfs import InsecureClient
import pandas as pd
from datetime import datetime

client = InsecureClient("http://"+TwitterCredentials.HOST_IP+":50070", user=TwitterCredentials.USER)  #Dirrect link to the namenode utilities


def WriteDataHadoop(dataList):  #Will creade csv format file with 3 columns: Test; SentimentalAnalysisResult; Prediction score, and fill the rows with Twitter data
    try:
        list_text = []
        list_result = []
        list_score = []
        for item in dataList:
            list_text.append(item[0])
            list_result.append(item[1][0])
            list_score.append(item[1][1])
        DataFrame = pd.DataFrame(data={"Text":
        list_text, "SentimentResult":list_result, "Prediction_score": list_score})
        with client.write("/user/hdfs/TBG/warehouse/"+
        str(datetime.now()).replace(" ", "_").replace(":", ".")+
        ".csv", encoding='utf-8') as writer:
            DataFrame.to_csv(writer)
    except Exception as e:
        print("Something went wrong..." + str(e))





