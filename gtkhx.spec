Summary:	GtkHx is a GTK+ version of Hx, a UNIX Hotline Client.
Name:		gtkhx
Version:	0.8.10
Release:	1
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
License:	GPL
URL:		http://gtkhx.sourceforge.net/
Source0:	http://gtkhx.sourceforge.net/files/%{name}-%{version}.tar.gz
#Provides: none
Requires:	gtk+
Requires:	glib
Requires:	gdk-pixbuf
#Conflicts: none
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkHx is a GTK+ version of Hx, a UNIX Hotline Client.

%prep

%setup

%build
./configure


%{__make}
%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/share/gtkhx/sounds
make install prefix=$RPM_BUILD_ROOT/usr
#install gtkhx_pixmap.png $RPM_BUILD_ROOT/usr/share/gtkhx/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtkhx
%{_datadir}/gtkhx/icons.rsrc
%{_datadir}/gtkhx/sounds/chatinvite.aiff
%{_datadir}/gtkhx/sounds/chatpost.aiff
%{_datadir}/gtkhx/sounds/error.aiff
%{_datadir}/gtkhx/sounds/filedone.aiff
%{_datadir}/gtkhx/sounds/join.aiff
%{_datadir}/gtkhx/sounds/logged-in.aiff
%{_datadir}/gtkhx/sounds/message.aiff
%{_datadir}/gtkhx/sounds/newspost.aiff
%{_datadir}/gtkhx/sounds/part.aiff
%{_datadir}/gtkhx/gtkhx_pixmap.png

%doc README COPYING ChangeLog BUGS AUTHORS TODO DOCUMENTATION
