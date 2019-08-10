import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'skystats-profile-menu',
  templateUrl: './profile-menu.component.html',
  styleUrls: ['./profile-menu.component.scss']
})
export class ProfileMenuComponent implements OnInit {
  @Input()
  name: string;

  @Input()
  image: string;

  @Output()
  loggedOut = new EventEmitter();

  constructor() { }

  ngOnInit() {
  }

  logout() {
    this.loggedOut.emit();
  }

}
