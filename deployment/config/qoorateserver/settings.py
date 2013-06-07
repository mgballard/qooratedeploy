# our general app settings
app = {
    ## Our long polling interval
    ## not used yet
    "POLLING_INTERVAL": 15,
    
    ## The base URI to access the API server
    ## not used yet
    "QOORATE_API_URI": "http://beta.qrate.co/q",

    ## The URI to the qrate homepage, for humans not machines
    "QOORATE_URI": "http://beta.qrate.co",

    ## Amazon info for linking
    "S3_IMG_PATH": "https://s3.amazonaws.com/<<bucket>>/",

    ## Amazon info needed to insert image into table
    ## not really used right now
    "AMAZON_BUCKET": '<<bucket>>',
        
    ## Replace not found images with this value
    "BROKEN_IMG_URI": "http://beta.qrate.co/q/img/blank.gif",

    ## Our defaul paging values
    "PARENT_PAGE_SIZE": 5,
    "CHILD_PAGE_SIZE": 5,

    ## Temporary directory
    ## no trailing slash
    "TEMP_DIR": "tmp",       
}

uploader = {
    ## Amazon info for S3 file uploads
    "AMAZON_KEY": '<<key>>',
    "AMAZON_SECRET": '<<secret>>',
    "AMAZON_BUCKET": '<<bucket>>',
    ## no trailing slash
    "TEMP_UPLOAD_DIR": "tmp",

    ## The size of our image we createwhen we upload and send to S3
    # (size, PIL format, postfix, extension)
    # if size is None, we save full size
    "IMAGE_INFO": [ (None,"JPEG",'_f',"jpg"),
                    ((300,200),"JPEG",'_t',"jpg"),
                    ((120,200),"JPEG",'_m',"jpg"),
                    ((170,100),"JPEG",'_f',"jpg"),
                    ((50,50),"JPEG",'_s',"jpg"),
    ],

    "ACCEPTABLE_UPLOAD_MIME_TYPES": ["image/jpeg","image/gif","image/png"],

}

# Our oauth settings
oauth = {
    ## Do not really do auth, fake it
    "OAUTH_TEST": False,

    "REDIS": {
        "SERVER": "localhost",
        "PORT": 3306,
        "USERNAME": "<<username>>",
        "PASSWORD": "<<password>>",
        "DATABASE": "<<db>>",
    },

    # Configuration of supported providers
    "PROVIDERS": {
        "facebook": {
            "PROVIDER_NAME": "facebook",
            "PROVIDER_TAG": "fb",
            "OAUTH_VERSION": "2.0",
            "APP_ID": "<<APPID>>",
            "APP_SECRET": "<<APPSECRET>>",
            "SCOPE": "user_about_me, email, user_location, publish_stream",
            "REDIRECT_URL": "http://beta.qrate.co/q/oauth/facebook/callback",
            "REQUEST_URL": "https://www.facebook.com/dialog/oauth",
            "REQUEST_URL_ADDITIONAL_PARAMS": {"display" : "popup"}, 
            "ACCESS_TOKEN_REQUEST_URL": "https://graph.facebook.com/oauth/access_token",
            "USER_INFO": [  
                ["https://graph.facebook.com/me", 
                    [
                        ["username", ["username"]], 
                        ["name", ["name"]], 
                        ["fullname", [["first_name"],["last_name"]], "%s %s"], 
                        ["oauth_uid", ["id"]],
                        ["thumbnailLarge", ["id"], "https://graph.facebook.com/%s/picture"],
                    ],
                ],
            ],
            "ALIASES": [  
                ["oauth_access_token", ["access_token"]],
            ],

            "TEST_OAUTH_DATA": { 
                "username": "<<USERNAME>>", 
                "first_name": "Seth", 
                "last_name": "Murphy", 
                "verified": True, 
                "name": "Seth Murphy", 
                "access_token": "<<TOKEN>>", 
                "expires": "6021", 
                "updated_time": "2011-12-26T11:18:15+0000", 
                "locale": "en_US", 
                "link": "http://www.facebook.com/sethmurph", 
                "timezone": -5, 
                "work": [{"position": {"id": "148485888500795", "name": "Founder"}, "description": "Think Globally, Develop Locally", "location": {"id": "112111905481230", "name": "Brooklyn, New York"}, "start_date": "2011-03", "employer": {"id": "171723742885121", "name": "Brooklyn Code Incorporated"}}], 
                "id": "1276883229"
            },
        },

        "twitter": {
            "PROVIDER_NAME": "twitter",
            "PROVIDER_TAG": "tw",
            "OAUTH_VERSION": "1.0a",
            "CONSUMER_KEY": "<<CONSUMERKEY>>",
            "CONSUMER_SECRET": "<<SECRET>>",
            "REQUEST_TOKEN_URL": "https://api.twitter.com/oauth/request_token",
            "REQUEST_TOKEN_URL_HOST": "https://api.twitter.com",
            "REQUEST_TOKEN_URL_PATH": "/oauth/request_token",
            "AUTHORIZE_URL": "https://api.twitter.com/oauth/authorize",
            "ACCESS_TOKEN_URL": "https://api.twitter.com/oauth/access_token",
            "CALLBACK_URL": "http://beta.qrate.co/q/oauth/twitter/callback",
            "USER_INFO": [  
                ["https://api.twitter.com/1/account/verify_credentials.json", 
                    [
                        ["username", ["screen_name"]], 
                        ["email", ["screen_name"]], 
                        ["oauth_uid", ["id"]],
                        ["thumbnailLarge", ["profile_image_url"]],
                    ],
                ],
            ],
            "ALIASES": [  
                ["fullname", ["name"]],
                ["oauth_access_token", ["oauth_token"]],
            ],
        },

        "googleplus": {
            "PROVIDER_NAME": "googleplus",
            "PROVIDER_TAG": "gp",
            "OAUTH_VERSION": "2.0",
            "APP_ID": "<<APPID>>,
            "APP_SECRET": "<<APPSECRET>>",
            "SCOPE": "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email",
            "REDIRECT_URL": "http://beta.qrate.co/q/oauth/googleplus/callback",
            "REQUEST_URL": "https://accounts.google.com/o/oauth2/auth",
            "REQUEST_URL_ADDITIONAL_PARAMS": {"response_type" : "code"},
            "ACCESS_TOKEN_REQUEST_URL": "https://accounts.google.com/o/oauth2/token",
            "ACCESS_TOKEN_REQUEST_ADDITIONAL_PARAMS": {"grant_type" : "authorization_code"},
            "USER_INFO": [  
                ["https://www.googleapis.com/oauth2/v1/userinfo", 
                    [
                        ["username", ["name"]], 
                        ["oauth_uid", ["id"]],
                        ["thumbnailLarge", ["picture"]],
                        ["oauth_access_token", ["access_token"]],
                    ],
                ],
            ],
            "ALIASES": [  
                ["name", ["username"]],
                ["fullname", ["username"]],
            ],
            "TEST_OAUTH_DATA": { 
                "username": "sethmurph", 
                "first_name": "Seth", 
                "last_name": "Murphy", 
                "verified": True, 
                "name": "Seth Murphy", 
                "access_token": "AAADp76u74OwBAOkELCi8wtbD4YBiPBpHIhYkZBZCKIzFjm49Jrq6NNAZAJN9ZCSvXvNEnjTdED1nW6VdZCcZAlpkZB2ZBi5dvB6MeQeqaoZBGm2UscZB2MLb2p", 
                "expires": "6021", 
                "updated_time": "2011-12-26T11:18:15+0000", 
                "locale": "en_US", 
                "link": "http://www.facebook.com/sethmurph", 
                "timezone": -5, 
                "work": [{"position": {"id": "148485888500795", "name": "Founder"}, "description": "Think Globally, Develop Locally", "location": {"id": "112111905481230", "name": "Brooklyn, New York"}, "start_date": "2011-03", "employer": {"id": "171723742885121", "name": "Brooklyn Code Incorporated"}}], 
                "id": "1276883229"
            },
        },
    }
}

# our mysql settings
mysql = {
    "DEBUG": False,                    ## Not using yet
    "CONNECTION": {
        "HOST": "localhost",           ## MySQL Host
        "PORT": 3306,                  ## MySQL Post
        "USER": "<<USERNAME>>",             ## MySQL User
        "PASSWORD": "<<PASSWORD>>",         ## MySQL Password
        "DATABASE": "<<DB>>",         ## Database Name
        "COLLATION": 'utf8',           ## Database Collation
    },
    "TABLES": { ## Just used to alias fields instead of changing them in the database for now
        "COMMENT":{
            "TABLE_NAME": "q_[api_key]_images",
            "FIELDS": [
                'id',
                'locationId', 
                'relatedId', 
                'parentId', 
                'userId', 
                'type', 
                'name', 
                'location', 
                'description',
                'voteCount', 
                'voteNumber', 
                'votesUp', 
                'votesDown', 
                'flagCount', 
                'sortOrder', 
                'status', 
                'thumbnailSmall', 
                'thumbnailLarge', 
                'referer', 
                'changeDate', 
                'createDate',
            ],
            "FIELDS_MUTEABLE": [
                'name', 
                'location', 
                'description',
                'voteCount', 
                'voteNumber', 
                'votesUp', 
                'votesDown', 
                'flagCount', 
                'sortOrder', 
                'status', 
                'thumbnailSmall', 
                'thumbnailLarge', 
                'referer', 
                'changeDate', 
            ],
        },

        "KEYPAIR": {
            "TABLE_NAME": "keypair",
            "FIELDS": [
                'id',
                'key',
                'secret',
            ],
            "FIELDS_MUTEABLE": [
                'secret',
            ],
        },

        "QOORATE": {
            "TABLE_NAME": "qoorates",
            "FIELDS": [
                'id',
                'userId',
                'shortTitle',
                'longTitle',
                'url',
                'preferences',
                'description',
                'fieldNames',
                'refTable',
                'hasCat',
                'hasLoc',
                'hasPrice',
                'hasDesc',
                'createDate',
                'changeDate',
                'catNames',
                'catAllowed',
                'thumbnailSmall',
                'thumbnailLarge',
            ],
            "FIELDS_MUTEABLE": [
                'longTitle',
                'url',
                'preferences',
                'description',
                'fieldNames',
                'refTable',
                'hasCat',
                'hasLoc',
                'hasPrice',
                'hasDesc',
                'changeDate',
                'catNames',
                'catAllowed',
                'thumbnailSmall',
                'thumbnailLarge',
            ],
        },

        "FLAG": {
            "TABLE_NAME": "flag",
            "FIELDS": [
                'id',
                'refTable',
                'itemId',
                'userId',
                'flagTypeId',
                'createDate',
            ],
            "FIELDS_MUTEABLE": [
                'flagTypeId',
            ],
        },

        "FLAG_TYPE": {
            "TABLE_NAME": "flag_type",
            "FIELDS": [
                'id',
                'createDate',
                'name',
                'description',
            ],
            "FIELDS_MUTEABLE": [
                'flagTypeId',
            ],
        },

        "VOTE": {
            "TABLE_NAME": "vote",
            "FIELDS": [
                'id',
                'refTable',
                'itemId',
                'userId',
                'qootid',
                'up',
                'down',
                'createDate',
            ],
            "FIELDS_MUTEABLE": [
                'up',
                'down',
            ],
        },

        "IMAGE": {
            "TABLE_NAME": "q_[api_key]_images",
            "FIELDS": [
                'id',
                'itemId',
                's3Bucket',
                'thumbnailLargeHash',
            ],
            "FIELDS_MUTEABLE": [
                's3Bucket',
                'thumbnailLargeHash',
            ],
        },

        "USER": {
            "TABLE_NAME": "user",
            "FIELDS": [
                'id',
                'role',
                'email',
                'password',
                'oauth_provider',
                'oauth_uid',
                'username',
                'location',
                'changeDate',
                'createDate',
                'thumbnailSmall',
                'thumbnailLarge',
                'oauth_session_id',
                'oauth_access_token',
                'oauth_data',
            ],
            "FIELDS_MUTEABLE": [
                'role',
                'email',
                'password',
                'oauth_provider',
                'oauth_uid',
                'username',
                'location',
                'changeDate',
                'thumbnailSmall',
                'thumbnailLarge',
                'oauth_session_id',
                'oauth_access_token',
                'oauth_data',
            ],
        },
    }
}
