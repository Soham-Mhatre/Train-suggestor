import pandas as pd
import mysql.connector
import networkx as nx

ch=int(input("1.Mumbai Local 2.Indian Railways"))

if(ch==1):
    df=pd.read_csv("data.csv")
    db=config={
        'user':'root',
        'password':'root',
        'host':'localhost',
        'database':'train_data'
    }
    data = [
        ("Churchgate", "CCG", "Western", 0, 0),
        ("Marine Lines", "MEL", "Western", 1, 3),
        ("Charni Road", "CYR", "Western", 1, 2),
        ("Grant Road", "GTR", "Western", 1, 3),
        ("Mumbai Central", "MMCT", "Western", 1, 2),
        ("Mahalakshmi", "MX", "Western", 1, 3),
        ("Lower Parel", "PL", "Western", 2, 3),
        ("Prabhadevi", "PBHD", "Western", 1, 3),
        ("Dadar", "D/DR/DDR", "Western", 1, 2),
        ("Matunga Road", "MRU", "Western", 2, 2),
        ("Mahim Jn", "MM", "Western", 1, 3),
        ("Bandra", "B/BA", "Western", 2, 4),
        ("Khar Road", "KHAR", "Western", 2, 3),
        ("Santacruz", "STC", "Western", 1, 2),
        ("Vile Parle", "VLP", "Western", 2, 3),
        ("Andheri", "A/AD/ADH", "Western", 2, 5),
        ("Jogeshwari", "JOS", "Western", 2, 3),
        ("Ram Mandir", "RMAR", "Western", 2, 3),
        ("Goregaon", "GMN", "Western", 3, 2),
        ("Malad", "MDD", "Western", 2, 4),
        ("Kandivali", "KLE", "Western", 1, 3),
        ("Borivali", "BO/BVI", "Western", 3, 6),
        ("Dahisar", "DIC", "Western", 2, 5),
        ("Mira Road", "MIRA", "Western", 3, 5),
        ("Bhayander", "BY", "Western", 3, 5),
        ("Naigaon", "NIG", "Western", 6, 6),
        ("Vasai Road", "BSR/BS", "Western", 4, 5),
        ("Nalla Sopara", "NSP", "Western", 4, 5),
        ("Virar", "VR", "Western", 4, 6),
        ("Vaitarna", "VTN", "Western", 8, 9),
        ("Saphale", "SAH", "Western", 8, 8),
        ("Kelve Road", "KLV", "Western", 6, 8),
        ("Palghar", "PLG", "Western", 8, 15),
        ("Umroli Road", "UOI", "Western", 6, 6),
        ("Boisar", "BOR", "Western", 6, 6),
        ("Vangaon", "VGN", "Western", 9, 9),
        ("Dahanu Road", "DRD", "Western", 12, 13),
        ("CSMT", "CSMT/ST", "Central", 0, 0),
        ("Masjid", "MSD", "Central", 1, 3),
        ("Sandhurst Road", "SNRD", "Central", 1, 2),
        ("Byculla", "BY", "Central", 2, 3),
        ("Chinchpokli", "CHG", "Central", 1, 2),
        ("Currey Road", "CRD", "Central", 1, 2),
        ("Parel", "PR", "Central", 2, 3),
        ("Dadar", "D/DR/DDR", "Central", 1, 3),
        ("Matunga", "MTN", "Central", 1, 3),
        ("Sion", "SIN", "Central", 1, 4),
        ("Kurla", "C/CH", "Central", 1, 4),
        ("Vidhyavihar", "VVH", "Central", 2, 3),
        ("Ghatkopar", "G", "Central", 2, 3),
        ("Vikhroli", "VK", "Central", 4, 5),
        ("Kanjur Marg", "KJMG", "Central", 2, 3),
        ("Bhandup", "BND", "Central", 2, 3),
        ("Nahur", "NHU", "Central", 1, 3),
        ("Mulund", "MLND", "Central", 2, 3),
        ("Thane", "TNA", "Central", 2, 4),
        ("Kalva", "KLVA", "Central", 2, 4),
        ("Mumbra", "MBQ", "Central", 3, 6),
        ("Diva Jn", "DIVA", "Central", 3, 4),
        ("Kopar", "KOPR", "Central", 4, 5),
        ("Dombivli", "DI", "Central", 1, 3),
        ("Thakurli", "THK", "Central", 1, 3),
        ("Kalyan", "KYN", "Central", 3, 6),
        ("Vithalwadi", "VLDI", "Central", 2, 5),
        ("Ulhas Nagar", "ULNR", "Central", 1, 3),
        ("Ambernath", "ABH", "Central", 3, 6),
        ("Badalpur", "BUD", "Central", 7, 8),
        ("Vangani", "VGI", "Central", 11, 9),
        ("Shelu", "SHLU", "Central", 4, 4),
        ("Neral", "NRL", "Central", 4, 4),
        ("Bhivpuri Road", "BVS", "Central", 7, 7),
        ("Karjat", "KJT/S", "Central", 7, 9),
        ("Palasdhari", "PDI", "Central", 3, 5),
        ("Kelavli", "KLY", "Central", 5, 7),
        ("Dolavli", "DLV", "Central", 1, 3),
        ("Lowjee", "LWJ", "Central", 3, 4),
        ("Khopoli", "KP", "Central", 3, 6),
        ("Shahad", "SHAD", "Central", 2, 3),
        ("Ambivli", "ABY", "Central", 2, 2),
        ("Titwala", "TLA", "Central", 6, 5),
        ("Khadavli", "KDV", "Central", 8, 7),
        ("Vasind", "VSD", "Central", 5, 5),
        ("Asangaon", "ASO", "Central", 5, 4),
        ("Atgaon", "ATG", "Central", 6, 6),
        ("Thansit", "THS", "Central", 5, 5),
        ("Khardi", "KE", "Central", 8, 8),
        ("Umbermali", "OMB", "Central", 7, 7),
        ("Kasara", "KSRA", "Central", 6, 7),
        ("Panvel", "PNVL", "Harbour", 0, 0),
        ("Panvel", "PNVL", "Trans Harbour", 0, 1),
        ("Khandeshwar", "KDW", "Harbour", 1, 3),
        ("Mansarovar", "MNSR", "Harbour", 2, 3),
        ("Kharghar", "KHAG", "Harbour", 2, 3),
        ("Belapur CBD", "BEPR", "Harbour", 2, 3),
        ("Seawoods Darave", "SWDV", "Harbour", 2, 3),
        ("Nerul", "NEU", "Harbour", 2, 3),
        ("Juinagar", "JNJ", "Harbour", 2, 3),
        ("Sanpada", "SNCR", "Harbour", 1, 3),
        ("Vashi", "VSH", "Harbour", 2, 3),
        ("Mankhurd", "MNKD", "Harbour", 2, 3),
        ("Govandi", "GV", "Harbour", 1, 2),
        ("Chembur", "CHMB", "Harbour", 1, 2),
        ("Tilak Nagar", "TKNG", "Harbour", 2, 2),
        ("Kurla", "C/CH", "Harbour", 1, 2),
        ("Chunabhatti", "CHF", "Harbour", 1, 2),
        ("GTB Nagar", "GTBN", "Harbour", 1, 2),
        ("Vadala Road", "VDLR", "Harbour", 2, 3),
        ("Kings Circle", "KCE", "Harbour", 1, 2),
        ("Mahim", "MH", "Harbour", 2, 3),
        ("Thane", "TNA", "Trans Harbour", 0, 0),
        ("Airoli", "AIRL", "Trans Harbour", 8, 8),
        ("Rabale", "RABE", "Trans Harbour", 3, 3),
        ("Ghansoli", "GNSL", "Trans Harbour", 3, 3),
        ("Koparkhairane", "KPHN", "Trans Harbour", 3, 3),
        ("Turbhe", "TUH", "Trans Harbour", 4, 4),
        ("Juinagar", "JNJ", "Trans Harbour", 5, 5),
        ("Nerul", "NEU", "Trans Harbour", 3, 3),
        ("Seawood Darave", "SWDV", "Trans Harbour", 3, 3),
        ("Belapur CBD", "BEPR", "Trans Harbour", 4, 4),
        ("Kharghar", "KHAG", "Trans Harbour", 4, 4),
        ("Mansarovar", "MANR", "Trans Harbour", 3, 3),
        ("Khandeshwar", "KNDS", "Trans Harbour", 3, 3),
        ("Panvel", "PNVL", "Trans Harbour", 3, 3),
        ("Nerul", "NEU", "Uran", 0, 0),
        ("Seawood Darave", "SWDV", "Uran", 3, 3),
        ("Belapur CBD", "BEPR", "Uran", 4, 4),
        ("Bamandongri", "BMNDG", "Uran", 9, 12),
        ("Kharkopar", "KARP", "Uran", 3, 4),
        ("Neral", "NRL", "Neral-Matheran", 0, 0),
        ("Jumapatti", "JTT", "Neral-Matheran", 5, 46),
        ("Waterpipe", "WTP", "Neral-Matheran", 6, 46),
        ("Aman Lodge", "AMNA", "Neral-Matheran", 7, 50),
        ("Matheran", "MAE", "Neral-Matheran", 2, 18)
    ]
    graph = {}

    def add_edge(graph, from_node, to_node, distance, time):
        if from_node not in graph:
            graph[from_node] = {}
        graph[from_node][to_node] = {'distance': distance, 'time': time}

    for i in range(len(data) - 1):
        station, code, line, distance, time = data[i]
        next_station, next_code, next_line, next_distance, next_time = data[i + 1]

        if line == next_line:
            from_node = (station, line)
            to_node = (next_station, next_line)
            add_edge(graph, from_node, to_node, next_distance, next_time)
            add_edge(graph, to_node, from_node, next_distance, next_time)



    station_line_map = {}
    for station, code, line, distance, time in data:
        if station not in station_line_map:
            station_line_map[station] = []
        station_line_map[station].append(line)

    for station, lines in station_line_map.items():
        for i in range(len(lines)):
            for j in range(i + 1, len(lines)):
                from_node = (station, lines[i])
                to_node = (station, lines[j])
                add_edge(graph, from_node, to_node, 0, 0)
                add_edge(graph, to_node, from_node, 0, 0)


    conn = mysql.connector.connect(**db)
    cursor = conn.cursor()

    check_query = """
    SELECT COUNT(*) FROM trains3 WHERE Station = %s AND Station_code = %s
    """

    insert_query = """
    INSERT INTO trains3 (Station, Station_code, Line, Distance_from_prev_line, Time_taken_from_previous_line)
    VALUES (%s, %s, %s, %s, %s)
    """
    for i, row in df.iterrows():
        cursor.execute(check_query, (row['Station'], row['Station_Code']))
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.execute(insert_query, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()


    def find_shortest_path(graph, src, src_line, dest, dest_line):
        start_node = (src, src_line)
        end_node = (dest, dest_line)

        try:
            # Find all paths from start_node to end_node
            all_paths = list(nx.all_shortest_paths(graph, source=start_node, target=end_node, weight='distance'))

            # Filter out paths with unnecessary line changes
            def is_valid_path(path):
                for i in range(len(path) - 1):
                    if path[i][0] == path[i + 1][0] and graph[path[i]][path[i + 1]]['distance'] == 0:
                        continue
                    if path[i][1] != path[i + 1][1] and graph[path[i]][path[i + 1]]['distance'] != 0:
                        return False
                return True

            valid_paths = list(filter(is_valid_path, all_paths))

            # Select the first valid path (as all paths are shortest due to all_shortest_paths)
            shortest_path = valid_paths[0]

            print(f"Shortest path: {shortest_path[0][0]}({shortest_path[0][1]})->",end=" ")
            for i in range(len(shortest_path)-1):
                if(shortest_path[i][0]==shortest_path[i+1][0]):
                    print(f"{shortest_path[i][0]}({shortest_path[i][1]})->",end=" ")
                    print(f"{shortest_path[i+1][0]}({shortest_path[i+1][1]})->",end=" ")

            print(f"{shortest_path[-1][0]}({shortest_path[-1][1]})")
        except nx.NetworkXNoPath:
            print(f"No path found between {src} ({src_line}) and {dest} ({dest_line})")

    G = nx.DiGraph()

    for node, neighbors in graph.items():
        for neighbor, info in neighbors.items():
            G.add_edge(node, neighbor, distance=info['distance'], time=info['time'])

    start_station = input("Enter the starting station: ")
    start_line = input("Enter the starting line: ")
    end_station = input("Enter the destination station: ")
    end_line = input("Enter the destination line: ")

    find_shortest_path(G, start_station, start_line, end_station, end_line)

elif(ch==2):
    import pandas as pd
    import mysql.connector

    dr = pd.read_csv("train_info.csv")

    db = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'database': 'train_data'
    }

    conn = mysql.connector.connect(**db)
    cursor = conn.cursor()

    check_query = "SELECT COUNT(*) FROM irdata1"
    insert_query = """
    INSERT INTO irdata1 (Train_no, Train_name, Source_station, Destination_station, Days)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(check_query)
    count = cursor.fetchone()[0]

    if count == 0:
        for i, row in dr.iterrows():
            cursor.execute(insert_query, tuple(row))


    ch=int(input("1.Search by station 2.Search by PNR number"))
    if(ch==1):
        src = input("Enter source station: ")
        dest = input("Enter destination station: ")


        check_query1 = """
        SELECT * FROM irdata1 WHERE Source_station = %s AND Destination_station = %s
        """

        cursor.execute(check_query1, (src, dest))
        result = cursor.fetchall()
        if len(result) == 0: 
            print("No results found") 
        else: 
            for row in result: print(row)
    elif(ch==2):
        pnr=int(input("Enter PNR number"))
        check_query2 = """
        SELECT * FROM irdata1 WHERE Train_no =%s
        """

        cursor.execute(check_query2,(pnr,))
        result = cursor.fetchall()
        if len(result) == 0: 
            print("No results found") 
        else: 
            for row in result: print(row)

    conn.commit()
    cursor.close()
    conn.close()
    print("Done")
