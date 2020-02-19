# Fix a p:
exec { 'modify_file':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/bin'
}
