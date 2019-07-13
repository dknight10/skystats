import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'skystats-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.scss']
})
export class SidenavComponent implements OnInit {
  views = [
    { name: 'Sessions', url: '' },
  ]

  constructor() { }

  ngOnInit() {
  }

}
