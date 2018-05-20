class SelectModel(object):
    def define_model(model):
        cols_to_remove = []
        ranges = []
        words = []        

        if model == "mm3":
            cols_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14,
                                                  16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39,
                                                  40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm3_more":
            cols_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14,
                                                  16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39,
			  40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_cons":
            cols_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14,
                                          16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39,
		          40, 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm3_cons_more":
            cols_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14,
                                                 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_cons_3":
            cols_to_remove = [3, 4, 8, 9, 13, 14,
                                                 18, 19, 23, 24, 28, 29, 33, 34, 38, 39,
                                                 40, 41, 42, 43, 44, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm3_cons_3_more":
            cols_to_remove = [3, 4, 8, 9, 13, 14,
                                                 18, 19, 23, 24, 28, 29, 33, 34, 38, 39,
                                                 40, 41, 42, 43, 44, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_cons_5":
            cols_to_remove = [40, 41, 42, 43, 44]
            ranges = []
            words = ["no", "no"]
        if model == "mm3_cons_5_more":
            cols_to_remove = [40, 41, 42, 43, 44]
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_cons_solv":
            cols_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14,
                                         16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39,
		         41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm3_cons_solv_more":
            cols_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14,
                                         16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39,
		         41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_cons_solv_no_dist_more":
            cols_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                     16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39,
		     41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_cs_3":
            cols_to_remove = [3, 4, 8, 9, 13, 14,
                                                 18, 19, 23, 24, 28, 29, 33, 34, 38, 39,
                                                 43, 44, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm3_cs_3_more":
            cols_to_remove = [3, 4, 8, 9, 13, 14,
                                                 18, 19, 23, 24, 28, 29, 33, 34, 38, 39,
                                                 43, 44, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_cs_5":
            cols_to_remove = []
            ranges = []
            words = ["no", "no"]
        if model == "mm3_cs_5_more":
            cols_to_remove = []
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_3":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39, 
			40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm3_3_more":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_3_cons":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39,
			 40, 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm3_3_cons_more":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39,
			 40, 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_3_cons_solv":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm3_3_cons_solv_more": 
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_5":
            cols_to_remove = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm3_5_more":
            cols_to_remove = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_5_cons":
            cols_to_remove = [40, 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm3_5_cons_more":
            cols_to_remove = [40, 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_5_cons_solv":
            cols_to_remove = [41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm3_5_cons_solv_more":
            cols_to_remove = [41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm3_avg_lr":
            cols_to_remove = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,0], [1,2], [3,4], [5,5], [6,7], [8,9], [10,10], [11,12], [13,14], [15,15], [16,17], [18,19],
                          [20,20], [21,22], [23,24], [25,25], [26,27], [28,29], [30,30], [31,32], [33,34], [35,35], [36,37], [38,39]]
            words = ["yes", "no"]
        if model == "mm3_avg_lr_more":
            cols_to_remove = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,0], [1,2], [3,4], [5,5], [6,7], [8,9], [10,10], [11,12], [13,14], [15,15], [16,17], [18,19],
                          [20,20], [21,22], [23,24], [25,25], [26,27], [28,29], [30,30], [31,32], [33,34], [35,35], [36,37], [38,39]]
            words = ["yes", "yes"]
        if model == "mm3_avg":
            cols_to_remove = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,0], [1,4], [5,5], [6,9], [10,10], [11,14], [15,15], [16,19],
                          [20,20], [21,24], [25,25], [26,29], [30,30], [31,34], [35,35], [36,39]]
            words = ["yes", "no"]
        if model == "mm3_avg_more":
            cols_to_remove = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,0], [1,4], [5,5], [6,9], [10,10], [11,14], [15,15], [16,19],
                          [20,20], [21,24], [25,25], [26,29], [30,30], [31,34], [35,35], [36,39]]
            words = ["yes", "yes"]
        if model == "mm3_3_avg":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,0], [1,2], [3,3], [4,5], [6,6], [7,8], [9,9], [10,11], [12,12], [13,14], 
                                  [15,15], [16,17], [18,18], [19,20], [21,21], [22,23]]
            words = ["yes", "no"]
        if model == "mm3_3_avg_more":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,0], [1,2], [3,3], [4,5], [6,6], [7,8], [9,9], [10,11], [12,12], [13,14], 
                                  [15,15], [16,17], [18,18], [19,20], [21,21], [22,23]]
            words = ["yes", "yes"]
        if model == "mm3_cons_avg":
            cols_to_remove = [40, 41, 42, 43, 44]
            ranges = [[0,0],[1,4],[5,5],[6,9], [10,10], [11,14], [15,15], [16,19], [20,20], [21,24], [25,25], [26,29], [30,30],
                                  [31,34], [35,35], [36,39], [40,40], [41,44]]
            words = ["yes", "no"]
        if model == "mm3_cons_avg_more":
            cols_to_remove = [40, 41, 42, 43, 44]
            ranges = [[0,0],[1,4],[5,5],[6,9], [10,10], [11,14], [15,15], [16,19], [20,20], [21,24], [25,25], [26,29], [30,30],
                                  [31,34], [35,35], [36,39], [40,40], [41,44]]
            words = ["yes", "yes"]
        if model == "mm3_3_cons_avg":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39, 40, 41, 42, 43, 44, 48, 49]
            ranges = [[0,0],[1,2],[3,3],[4,5], [6,6], [7,8], [9,9], [10,11], [12,12], [13,14], [15,15], [16,17], [18,18],
                                  [19,20], [21,21], [22,23], [24,24], [25,26]]
            words = ["yes", "no"]
        if model == "mm3_3_cons_avg_more":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39, 40, 41, 42, 43, 44, 48, 49]
            ranges = [[0,0],[1,2],[3,3],[4,5], [6,6], [7,8], [9,9], [10,11], [12,12], [13,14], [15,15], [16,17], [18,18],
                                  [19,20], [21,21], [22,23], [24,24], [25,26]]
            words = ["yes", "yes"]
        if model == "mm3_cs_avg":
            cols_to_remove = []
            ranges = [[0,0], [1,4], [5,5], [6,9], [10,10], [11,14], [15,15], [16,19], [20,20], [21,24],
		  [25,25], [26,29], [30,30], [31,34], [35,35], [36,39], [40,40], [41,44], [45,45], [46,49]]
            words = ["yes","no"]
        if model == "mm3_cs_avg_more":
            cols_to_remove = []
            ranges = [[0,0], [1,4], [5,5], [6,9], [10,10], [11,14], [15,15], [16,19], [20,20], [21,24],
		  [25,25], [26,29], [30,30], [31,34], [35,35], [36,39], [40,40], [41,44], [45,45], [46,49]]
            words = ["yes","yes"]
        if model == "mm3_3_cs_avg":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39, 43, 44, 48, 49]
            ranges = [[0,0], [1,2], [3,3], [4,5], [6,6], [7,8], [9,9], [10,11], [12,12], [13,14],
		  [15,15], [16,17], [18,18], [19,20], [21,21], [22,23], [24,24], [25,26], [27,27], [28,29]]
            words = ["yes","no"]
        if model == "mm3_3_cs_avg_more":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39, 43, 44, 48, 49]
            ranges = [[0,0], [1,2], [3,3], [4,5],  [6,6], [7,8], [9,9], [10,11], [12,12], [13,14],
		  [15,15], [16,17], [18,18], [19,20], [21,21], [22,23], [24,24], [25,26], [27,27], [28,29]]
            words = ["yes","yes"]
        if model == "snap_center":
            cols_to_remove = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,4], [5,9], [10,14], [15,19],
                          [20,24], [25,29], [30,34], [35,35], [36,39]]
            words = ["yes", "no"]
        if model == "snap_center_more":
            cols_to_remove = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,4], [5,9], [10,14], [15,19],
                           [20,24], [25,29], [30,34], [35,35], [36,39]]
            words = ["yes", "yes"]
        if model == "snap_center_3":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,2], [3,5], [6,8], [9,11], [12,14], [15,17], [18,20], [21,21], [22,23]]
            words = ["yes", "no"]
        if model == "snap_center_3_more":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,2], [3,5], [6,8], [9,11], [12,14], [15,17], [18,20], [21,21], [22,23]]
            words = ["yes", "yes"]
        if model == "snap_evc_center":
            cols_to_remove = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,4], [5,9], [10,14], [15,19],
                          [20,24], [25,29], [30,30], [31,34], [35,35], [36,39]]
            words = ["yes", "no"]
        if model == "snap_evc_center_more":
            cols_to_remove = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,4], [5,9], [10,14], [15,19],
                          [20,24], [25,29], [30,30], [31,34], [35,35], [36,39]]
            words = ["yes", "yes"]
        if model == "snap_evc_center_3":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,2], [3,5], [6,8], [9,11], [12,14], [15,17], [18,18], [19,20], [21,21], [22,23]]
            words = ["yes", "no"]
        if model == "snap_evc_center_3_more":
            cols_to_remove = [3, 4, 8, 9, 13, 14, 18, 19, 23, 24, 28, 29, 33, 34, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [[0,2], [3,5], [6,8], [9,11], [12,14], [15,17], [18,18], [19,20], [21,21], [22,23]]
            words = ["yes", "yes"]
        if model == "mm4":
            cols_to_remove = [33, 34, 38, 39, 43, 44, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm4_more":
            cols_to_remove = [33, 34, 38, 39, 43, 44, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm4_avg":
            cols_to_remove = [33, 34, 38, 39, 43, 44, 48, 49]
            ranges = [[0,0], [1,4], [5,5], [6,9], [10,10], [11,14], [15,15], [16,19], [20,20], [21,24], [25,25], [26,29],
                                  [30,30], [31,32], [33,33], [34,35], [36,36], [37,38], [39,39], [40,41]]
            words = ["yes", "no"]
        if model == "mm4_avg_more":
            cols_to_remove = [33, 34, 38, 39, 43, 44, 48, 49]
            ranges = [[0,0], [1,4], [5,5], [6,9], [10,10], [11,14], [15,15], [16,19], [20,20], [21,24], [25,25], [26,29],
                                  [30,30], [31,32], [33,33], [34,35], [36,36], [37,38], [39,39], [40,41]]
            words = ["yes", "yes"]
        if model == "mm_best":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14,
                                                  15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm_best_more":         
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14,
                                                  15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm_best_3":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14,
                                                  15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29,
                                                  33, 34, 38, 39, 43, 44, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm_best_3_more":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14,
                                                  15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29,
                                                  33, 34, 38, 39, 43, 44, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm_best_5":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                  15, 16, 17, 18, 19, 25, 26, 27, 28, 29]
            ranges = []
            words = ["no", "no"]
        if model == "mm_best_5_more":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                  15, 16, 17, 18, 19, 25, 26, 27, 28, 29]
            ranges = []
            words = ["no", "yes"]
        if model == "mm_best_5_avg":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                  15, 16, 17, 18, 19, 25, 26, 27, 28, 29]
            ranges = [[0,0], [1,4], [5,5], [6,9], [10,10], [11,14], [15,15], [16,19], [20,20], [21,24], [25,25], [26,29]]
            words = ["yes", "no"]
        if model == "mm_best_5_avg_more":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                  15, 16, 17, 18, 19, 25, 26, 27, 28, 29]
            ranges = [[0,0], [1,4], [5,5], [6,9], [10,10], [11,14], [15,15], [16,19], [20,20], [21,24], [25,25], [26,29]]
            words = ["yes", "yes"]
        if model == "mm_best_3_avg":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14,
                                                  15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29,
                                                  33, 34, 38, 39, 43, 44, 48, 49]
            ranges = [[0,0], [1,2], [3,3], [4,5], [6,6], [7,8], [9,9], [10,11], [12,12], [13,14], [15,15], [16,17]]
            words = ["yes", "no"]
        if model == "mm_best_3_avg_more":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14,
                                                  15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29,
                                                  33, 34, 38, 39, 43, 44, 48, 49]
            ranges = [[0,0], [1,2], [3,3], [4,5], [6,6], [7,8], [9,9], [10,11], [12,12], [13,14], [15,15], [16,17]]
            words = ["yes", "yes"]
        if model == "mm3_5_wt_cum":
            cols_to_remove = [0, 1, 2, 3, 4, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm3_5_wt_cum_more":
            cols_to_remove = [0, 1, 2, 3, 4, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm":
            cols_to_remove = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "mm_more":
            cols_to_remove = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        if model == "mm_3":
            cols_to_remove = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "mm_3_more":
            cols_to_remove = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "yes"]
        if model == "mm_5":
            cols_to_remove = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "mm_5_more":
            cols_to_remove = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "yes"]
        if model == "mm2":
            cols_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "mm2_more":
            cols_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "yes"]
        if model == "mm2_3":
            cols_to_remove = [3, 4, 8, 9, 10, 11, 12, 13, 14, 
			18, 19, 23, 24, 25, 26, 27, 28, 29, 33, 34, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "mm2_3_more":
            cols_to_remove = [3, 4, 8, 9, 10, 11, 12, 13, 14, 
			18, 19, 23, 24, 25, 26, 27, 28, 29, 33, 34, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "yes"]
        if model == "mm2_5":
            cols_to_remove = [10, 11, 12, 13, 14, 
			25, 26, 27, 28, 29, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "mm2_5_more":
            cols_to_remove = [10, 11, 12, 13, 14, 
			25, 26, 27, 28, 29, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "yes"]
        if model == "mm3_cum":
            cols_to_remove = [6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "mm3_cum_more":
            cols_to_remove = [6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "yes"]
        if model == "cum":
            cols_to_remove = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cum_solv":
            cols_to_remove = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cum_dist":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 
	 		15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cum_3":
            cols_to_remove = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cum_solv_3":
            cols_to_remove = [0, 1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cum_dist_3":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = [] 
            words=["no", "no"]
        if model == "cum_5":
            cols_to_remove = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
                                           15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cum_solv_5":
            cols_to_remove = [0, 1, 2, 3, 4, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cum_dist_5":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cluster":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cluster_solv":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
			15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cluster_dist":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cluster_3":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cluster_solv_3":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
			15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cluster_dist_3":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cluster_5":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cluster_solv_5":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
			15, 16, 17, 18, 19, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cluster_dist_5":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "evmut":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "evmut_3":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 33, 34, 35, 36, 37, 38, 39,
			40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "evmut_5":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 35, 36, 37, 38, 39,
			40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "snap":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39,
			40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "snap_3":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 38, 39,
			 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "snap_5":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
			40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cons":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			 40, 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words=["no", "no"]
        if model == "cons_3":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			40, 41, 42, 43, 44, 48, 49]
            ranges = []
            words = ["no", "no"]
        if model == "cons_5":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
			15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
			40, 41, 42, 43, 44]
            ranges = []
            words = ["no", "no"]

        if model == "mm_no_dist":
            cols_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39,
                                                 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]

        if model == "mm_no_dist_3":
            cols_to_remove = [3, 4, 8, 9, 10, 11, 12, 13, 14,
                                                 18, 19, 23, 24, 25, 26, 27, 28, 29, 33, 34, 38, 39,
                                                 43, 44, 48, 49]
            ranges = []
            words = ["no", "no"]

        if model == "mm_no_dist_5":
            cols_to_remove = [10, 11, 12, 13, 14,
                                                 25, 26, 27, 28, 29]
            ranges = []
            words = ["no", "no"]

        if model == "mm_no_dist_more":
            cols_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39,
                                                 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]

        if model == "mm_no_dist_3_more":
            cols_to_remove = [3, 4, 8, 9, 10, 11, 12, 13, 14,
                                                 18, 19, 23, 24, 25, 26, 27, 28, 29, 33, 34, 38, 39,
                                                 43, 44, 48, 49]
            ranges = []
            words = ["no", "yes"]

        if model == "mm_no_dist_5_more":
            cols_to_remove = [10, 11, 12, 13, 14,
                                                 25, 26, 27, 28, 29]
            ranges = []
            words = ["no", "yes"]

        if model == "mm_no_evmut":
            cols_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14,
                                                 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39,
                                                 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "no"]

        if model == "mm_no_evmut_3":
            cols_to_remove = [3, 4, 8, 9, 13, 14,
                                                 18, 19, 23, 24, 28, 29, 30, 31, 32, 33, 34, 38, 39,
                                                 43, 44, 48, 49]
            ranges = []
            words = ["no", "no"]

        if model == "mm_no_evmut_5":
            cols_to_remove = [30, 31, 32, 33, 34]
            ranges = []
            words = ["no", "no"]

        if model == "mm_no_evmut_more":
            cols_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14,
                                                 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39,
                                                 41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]

        if model == "mm_no_evmut_3_more":
            cols_to_remove = [3, 4, 8, 9, 13, 14,
                                                 18, 19, 23, 24, 28, 29, 30, 31, 32, 33, 34, 38, 39,
                                                 43, 44, 48, 49]
            ranges = []
            words = ["no", "yes"]

        if model == "mm_no_evmut_5_more":
            cols_to_remove = [30, 31, 32, 33, 34]
            ranges = []
            words = ["no", "yes"]
        
        if model == "cons_solv_more":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                                                  41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"] 

        if model == "cons_solv_3_more":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
			  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                                                  43, 44, 48, 49]
            ranges = []
            words = ["no", "yes"]

        if model == "cons_solv_5_more":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
			  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
            ranges = []
            words = ["no", "yes"]

        if model == "snap_cons_solv_more":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  30, 31, 32, 33, 34, 36, 37, 38, 39,
                                                  41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
        
        if model == "snap_cons_solv_3":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  30, 31, 32, 33, 34, 38, 39,
                                                  43, 44, 48, 49]
            ranges = []
            words = ["no", "no"]

        if model == "snap_cons_solv_3_more":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  30, 31, 32, 33, 34, 38, 39,
                                                  43, 44, 48, 49]
            ranges = []
            words = ["no", "yes"]

        if model == "snap_cons_solv_5_more":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  30, 31, 32, 33, 34]
            ranges = []
            words = ["no", "yes"]

        if model == "evmut_cons_solv_more": 
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  31, 32, 33, 34, 35, 36, 37, 38, 39,
                                                  41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
 
        if model == "evmut_cons_solv_3_more": 
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  33, 34, 35, 36, 37, 38, 39,
                                                  43, 44, 48, 49]
            ranges = []
            words = ["no", "yes"]
 
        if model == "evmut_cons_solv_5_more": 
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  35, 36, 37, 38, 39]
            ranges = []
            words = ["no", "yes"]
 
        if model == "snap_evmut_cons_solv_more":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  31, 32, 33, 34, 36, 37, 38, 39,
                                                  41, 42, 43, 44, 46, 47, 48, 49]
            ranges = []
            words = ["no", "yes"]
 
        if model == "snap_evmut_cons_solv_3_more":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                                  33, 34, 38, 39,
                                                  43, 44, 48, 49]
            ranges = []
            words = ["no", "yes"]
 
        if model == "snap_evmut_cons_solv_5_more":
            cols_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
            ranges = []
            words = ["no", "yes"]
 
        return cols_to_remove, ranges, words
