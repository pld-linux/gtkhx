
Summary: GtkHx is a GTK+ version of Hx, a UNIX Hotline Client.
Name: gtkhx
Version: 0.8.10
Release: 1
Group: Applications
Copyright: GPL
Packager: misha@nasledov.com
URL: http://gtkhx.sourceforge.net/
Source0: http://gtkhx.sourceforge.net/files/gtkhx-0.8.10.tar.gz
#Provides: none
Requires: gtk+, glib, gdk-pixbuf
#Conflicts: none
BuildRoot: /tmp/gtkhx-0.8.10
%Description
GtkHx is a GTK+ version of Hx, a UNIX Hotline Client.
%Prep
%setup
%Build
./configure
make
%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/usr/share/gtkhx/sounds
make install prefix=$RPM_BUILD_ROOT/usr
#install gtkhx_pixmap.png $RPM_BUILD_ROOT/usr/share/gtkhx/

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(-,root,root)
/usr/bin/gtkhx
/usr/share/gtkhx/icons.rsrc
/usr/share/gtkhx/sounds/chatinvite.aiff
/usr/share/gtkhx/sounds/chatpost.aiff
/usr/share/gtkhx/sounds/error.aiff
/usr/share/gtkhx/sounds/filedone.aiff
/usr/share/gtkhx/sounds/join.aiff
/usr/share/gtkhx/sounds/logged-in.aiff
/usr/share/gtkhx/sounds/message.aiff
/usr/share/gtkhx/sounds/newspost.aiff
/usr/share/gtkhx/sounds/part.aiff
/usr/share/gtkhx/gtkhx_pixmap.png
%doc README COPYING ChangeLog BUGS AUTHORS TODO DOCUMENTATION
