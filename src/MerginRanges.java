/**
 * Created by Alestar on 1/17/2019.
 */

import java.util.*;


public class MerginRanges {

    public class Meeting {

        private int startTime;
        private int endTime;

        public Meeting(int startTime, int endTime) {
            // number of 30 min blocks past 9:00 am
            this.startTime = startTime;
            this.endTime   = endTime;
        }

        public int getStartTime() {
            return startTime;
        }

        public void setStartTime(int startTime) {
            this.startTime = startTime;
        }

        public int getEndTime() {
            return endTime;
        }

        public void setEndTime(int endTime) {
            this.endTime = endTime;
        }

        @Override
        public String toString() {
            return "Meeting{" + startTime +
                    ", " + endTime +
                    '}';
        }

    }

    public Meeting buildMeeting(int startTime, int endTime){

        return new Meeting(startTime,endTime);

    }

    public List<Meeting> mergeRanges(List<Meeting> meetings) {

        // make a copy so we don't destroy the input
        List<Meeting> sortedMeetings = new ArrayList<>();
        for (Meeting meeting: meetings) {
            Meeting meetingCopy = new Meeting(meeting.getStartTime(), meeting.getEndTime());
            sortedMeetings.add(meetingCopy);
        }

        // sort by start time
        Collections.sort(sortedMeetings, new Comparator<Meeting>() {
            @Override
            public int compare(Meeting m1, Meeting m2) {
                return m1.getStartTime() - m2.getStartTime();
            }
        });

        // initialize mergedMeetings with the earliest meeting
        List<Meeting> mergedMeetings = new ArrayList<>();
        mergedMeetings.add(sortedMeetings.get(0));

        for (Meeting currentMeeting : sortedMeetings) {

            Meeting lastMergedMeeting = mergedMeetings.get(mergedMeetings.size() - 1);

            // if the current meeting overlaps with the last merged meeting, use the
            // later end time of the two
            if (currentMeeting.getStartTime() <= lastMergedMeeting.getEndTime()) {
                lastMergedMeeting.setEndTime(Math.max(lastMergedMeeting.getEndTime(), currentMeeting.getEndTime()));

                // add the current meeting since it doesn't overlap
            } else {
                mergedMeetings.add(currentMeeting);
            }
        }

        return mergedMeetings;
    }

    public static void main(String[] args) {
        MerginRanges mr= new MerginRanges();
        List<Meeting> meetings = Arrays.asList(mr.buildMeeting(0,1), mr.buildMeeting(3, 5), mr.buildMeeting(4, 8), mr.buildMeeting(10, 12), mr.buildMeeting(9, 10));
        List<Meeting> merge= mr.mergeRanges(meetings);
        System.out.println(" The merge Meetings(Rage) result is: " + Arrays.toString(merge.toArray()));
    }
}
