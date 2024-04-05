
// Copyright (c) 2024 the CODERS Asylum project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

namespace Bot.Src.Interfaces
{
    /// <summary>
    /// Interface that all the Tasks must implement.
    /// </summary>
    public interface ITasks
    {
        /// <summary>
        /// Method to start the task.
        /// </summary>
        public void StartTask();

        /// <summary>
        /// Method to stop the task.
        /// </summary>
        public void StopTask();

        /// <summary>
        /// Method to check if the task should be executed based on some conditions.
        /// </summary>
        /// <returns>True if the task should be executed, false otherwise.</returns>
        public void ShouldExecute();

    }
}