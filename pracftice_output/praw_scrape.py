# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:34:31 2020

@author: willf
"""


#csv
subreddit = reddit.subreddit('spinalcordinjuries')
hot_python = subreddit.hot(limit = 10)

try:
    for submission in hot_python:
        if not submission.stickied:
            comments = submission.comments.list()#convert comments to list
            submission.comments.replace_more(limit=0)
            with open('output_spinal.txt', 'w', encoding="utf-8") as txt_file:
                with open('output_spinal_praw.csv', 'w', encoding="utf-8") as csv_file:
                    for comment in submission.comments:
                        if len(comment.replies) > 0:
                            for reply in comment.replies:
                                comment.refresh()
                                data = [submission.title, comment.body, reply.body] 
                                txt_file.write(str(data))
                                print(data)
                                
                                csv_writer = csv.writer(csv_file)
                                csv_writer.writerow(data)
                        else:
                            post_line = [submission.title, comment.body] 
                            txt_file.write(str(data))
                            print(data)
                            csv_writer = csv.writer(csv_file)
                            csv_writer.writerow(data)
                        #f.write(str(post_line[0], "," ,post_line[1]))
                        #writer = csv.writer(f)
                        #writer.writerow(post_line)
                    #if len(comment.replies) > 0:
                    #post_line = [submission.title, submission.ups, submission.downs, submission.likes, submission.visited, comment.parent(), comment.id, comment.body, submission.comments.relpies.id, submission.comment.relpies.body]
                    #print(post_line)                              
except AttributeError as e:
    print(str(e))
except UnicodeEncodeError as e:
    print(str(e))
                                
                #1             

"""
# streaming from reddit


#subreddit
#.title
#.ups
#.downs        
#.upvote
#.downvote
#.reply
#.subscribe
#.unsubscribe
.comments

['STR_FIELD', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
 '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
 '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
 '__str__', '__subclasshook__', '__weakref__', '_chunk', '_comments_by_id', '_fetch', '_fetch_data', '_fetch_info',
 '_fetched', '_kind', '_reddit', '_reset_attributes', '_safely_add_arguments', '_url_parts', '_vote', 
 'all_awardings', 'allow_live_comments', 'approved_at_utc', 'approved_by', 'archived', 'author', 'author_flair_background_color',
 'author_flair_css_class', 'author_flair_richtext', 'author_flair_template_id', 'author_flair_text', 
 'author_flair_text_color', 'author_flair_type', 'author_fullname', 'author_patreon_flair', 'author_premium', 'awarders',
 'banned_at_utc', 'banned_by', 'can_gild', 'can_mod_post', 'category', 'clear_vote', 'clicked', 'comment_limit', 'comment_sort',
 'comments', 'content_categories', 'contest_mode', 'created', 'created_utc', 'crosspost', 'delete', 'disable_inbox_replies', 
 'discussion_type', 'distinguished', 'domain', 'downs', 'downvote', 'duplicates', 'edit', 'edited', 'enable_inbox_replies',
 'flair', 'fullname', 'gild', 'gilded', 'gildings', 'hidden', 'hide', 'hide_score', 'id', 'id_from_url', 'is_crosspostable',
 'is_meta', 'is_original_content', 'is_reddit_media_domain', 'is_robot_indexable', 'is_self', 'is_video', 'likes',
 'link_flair_background_color', 'link_flair_css_class', 'link_flair_richtext', 'link_flair_text', 'link_flair_text_color', 
 'link_flair_type', 'locked', 'mark_visited', 'media', 'media_embed', 'media_only', 'mod', 'mod_note', 'mod_reason_by', 
 'mod_reason_title', 'mod_reports', 'name', 'no_follow', 'num_comments', 'num_crossposts', 'num_reports', 'over_18', '
 parent_whitelist_status', 'parse', 'permalink', 'pinned', 'post_hint', 'preview', 'pwls', 'quarantine', 'removal_reason',
 'removed_by', 'removed_by_category', 'reply', 'report', 'report_reasons', 'save', 'saved', 'score', 'secure_media', 
 'secure_media_embed', 'selftext', 'selftext_html', 'send_replies', 'shortlink', 'spoiler', 'stickied', 'subreddit', 
 'subreddit_id', 'subreddit_name_prefixed', 'subreddit_subscribers', 'subreddit_type', 'suggested_sort', 'thumbnail', 
 'thumbnail_height', 'thumbnail_width', 'title', 'top_awarded_type', 'total_awards_received', 'treatment_tags', 'unhide',
 'unsave', 'ups', 'upvote', 'upvote_ratio', 'url', 'url_overridden_by_dest', 'user_reports', 'view_count', 'visited', 
 'whitelist_status', 'wls']

#comments
.body
.replies
.list()

['MISSING_COMMENT_MESSAGE', 'STR_FIELD', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
 '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', 
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_extract_submission_id', 
 '_fetch', '_fetch_data', '_fetch_info', '_fetched', '_kind', '_reddit', '_replies', '_reset_attributes', 
 '_safely_add_arguments', '_submission', '_url_parts', '_vote', 'all_awardings', 'approved_at_utc', 
 'approved_by', 'archived', 'associated_award', 'author', 'author_flair_background_color', 'author_flair_css_class', 
 'author_flair_richtext', 'author_flair_template_id', 'author_flair_text', 'author_flair_text_color', 
 'author_flair_type', 'author_fullname', 'author_patreon_flair', 'author_premium', 'awarders', 'banned_at_utc', 
 'banned_by', 'block', 'body', 'body_html', 'can_gild', 'can_mod_post', 'clear_vote', 'collapse', 'collapsed', 
 'collapsed_because_crowd_control', 'collapsed_reason', 'comment_type', 'controversiality', 'created', 'created_utc',
 'delete', 'depth', 'disable_inbox_replies', 'distinguished', 'downs', 'downvote', 'edit', 'edited',
 'enable_inbox_replies', 'fullname', 'gild', 'gilded', 'gildings', 'id', 'id_from_url', 'is_root', 'is_submitter', 
 'likes', 'link_id', 'locked', 'mark_read', 'mark_unread', 'mod', 'mod_note', 'mod_reason_by', 'mod_reason_title', 
 'mod_reports', 'name', 'no_follow', 'num_reports', 'parent', 'parent_id', 'parse', 'permalink', 'refresh', 'removal_reason',
 'replies', 'reply', 'report', 'report_reasons', 'save', 'saved', 'score', 'score_hidden', 'send_replies', 'stickied', 
 'submission', 'subreddit', 'subreddit_id', 'subreddit_name_prefixed', 'subreddit_type', 'top_awarded_type', 'total_awards_received',
 'treatment_tags', 'uncollapse', 'unsave', 'ups', 'upvote', 'user_reports']
alt
#1
if len(comment.replies) > 0:
    for reply in comment.replies:
        print('Reply:' + reply.body)


"""