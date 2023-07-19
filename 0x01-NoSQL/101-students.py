#!/usr/bin/env python3
""" Top students """


def top_student(mongo_collection):
    """ return all students by aggergate sorted score """
    top_stds = mongo_collection.aggregate([
             {
                 "$project":
                 {
                     "name": "$name",
                     "averageScore": {"$avg": "$topics.score"}
                 }
             },
             {
                 "$sort": {"averageScore": -1}
             }
        ])
    return top_stds
