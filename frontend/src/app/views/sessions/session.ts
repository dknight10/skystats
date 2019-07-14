
export class Shot {
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

export class Session {
    name: string;
    timestamp: string;
    session_type: string;
    shots: Shot[];
}