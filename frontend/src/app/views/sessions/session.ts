
export interface Shot {
    id: number;
    shot_num: number;
    hand: string;
    ball_speed: number;
    launch_angle: number;
    back_spin: number;
    side_spin: number;
    side_angle: number;
    offline_distance: number;
    carry: number;
    roll: number;
    total: number;
    hang_time: number;
    descent_angle: number;
    peak_height: number;
    club_speed: number;
    pti: number;
    club: string
}

let CLUB_ABBR_MAPPING = {
    undefined: "und",
    driver: "D"
}

export class Session {
    constructor(
        public name: string,
        public timestamp: Date,
        public session_type: string,
        public shots: Shot[],
        public shots_count: number,
        public clubs_used: string[]
    ) { };

    get clubs_abbr() {
        return this.clubs_used.map(club => CLUB_ABBR_MAPPING[club])
    }
}

export class SessionCreator {
    static create(event: Session) {
        return new Session(
            event.name,
            new Date(event.timestamp),
            event.session_type,
            event.shots,
            event.shots_count,
            event.clubs_used
        )
    }
}