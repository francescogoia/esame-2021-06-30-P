from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
                select distinct Localization 
                from classification c
                order by Localization asc
                """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row["Localization"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
        select c1.Localization as l1, c2.Localization as l2,  count(distinct i.`Type`) as peso
        from classification c1 , classification c2, interactions i
        where ((c1.GeneID = i.GeneID1 and c2.GeneID = i.GeneID2) or (c2.GeneID = i.GeneID1 and c1.GeneID = i.GeneID2))  and c1.Localization != c2.Localization 
        group by c1.Localization, c2.Localization 

            """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append((row["l1"], row["l2"], row["peso"]))
        cursor.close()
        conn.close()
        return result
