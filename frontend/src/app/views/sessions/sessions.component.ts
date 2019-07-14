import { Component, OnInit } from '@angular/core';
import { SessionsService } from './sessions.service';
import { Session, Shot } from './session';
import { Observable } from 'rxjs';

@Component({
  selector: 'skystats-sessions',
  templateUrl: './sessions.component.html',
  styleUrls: ['./sessions.component.scss']
})
export class SessionsComponent implements OnInit {
  sessions: Observable<Session[]>;

  constructor(private service: SessionsService) { }

  ngOnInit() {
    this.sessions = this.service.getSessions();
  }

}
