// Copyright (c) 2024 the CODERS Asylum project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

namespace Bot.Lib.Handlers{

    /// <summary>
    /// Supported GitHub events.
    public enum GitHubEvents{
        /// <summary>
        /// Push event.
        /// </summary>
        push,
        pull_request,
        pull_request_review,
        pull_request_review_comment,
        issues,
        issue_comment,
        commit_comment,
        create,
        delete,
        rename,
        fork,
        ping,
        release,
        status,
        watch,
        member,

    }


    public class PullRequestHandler{
        public PullRequestHandler(){
            
        }
    }
}