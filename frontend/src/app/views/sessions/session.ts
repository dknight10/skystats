
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
    "undefined": "und",
    "driver": "D",
    "2 wood": "2w",
    "3 wood": "3w",
    "4 wood": "4w",
    "5 wood": "5w",
    "6 wood": "6w",
    "7 wood": "7w",
    "8 wood": "8w",
    "9 wood": "9w",
    "2 hybrid": "2h",
    "3 hybrid": "3h",
    "4 hybrid": "4h",
    "5 hybrid": "5h",
    "6 hybrid": "6h",
    "7 hybrid": "7h",
    "8 hybrid": "8h",
    "9 hybrid": "9h",
    "3 iron": "3i",
    "4 iron": "4i",
    "5 iron": "5i",
    "6 iron": "6i",
    "7 iron": "7i",
    "8 iron": "8i",
    "9 iron": "9i",
    "pw": "pw",
    "gw": "gw",
    "sw": "sw",
    "lw": "lw"
}

export class Session {
    constructor(
        public id: number,
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
        console.log(event)
        return new Session(
            event.id,
            event.name,
            new Date(event.timestamp),
            event.session_type,
            event.shots,
            event.shots_count,
            event.clubs_used
        )
    }
}