# Another comment:
exec {'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
