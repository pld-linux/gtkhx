Summary:	GtkHx is a GTK+ version of Hx, a UNIX Hotline Client
Summary(pl.UTF-8):	GtkHx - wersja GTK+ uniksowego klienta Hotline Hx
Name:		gtkhx
Version:	0.9.4
Release:	2
Group:		X11/Applications
License:	GPL
Source0:	http://gtkhx.sourceforge.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	d61d7dc2df66d934464e0bb8cd0fe45e
URL:		http://gtkhx.sourceforge.net/
BuildRequires:	gtk+-devel
BuildRequires:	gdk-pixbuf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GtkHx is a GTK+ version of Hx, a UNIX Hotline Client.

%description -l pl.UTF-8
GtkHx to wersja pod GTK+ programu Hx - uniksowego klienta Hotline.

%prep
%setup -q

%build
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/gtkhx/sounds}

%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix}
#install gtkhx_pixmap.png $RPM_BUILD_ROOT%{_datadir}/gtkhx

%find_lang gtkhx

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gtkhx.lang
%defattr(644,root,root,755)
%doc README ChangeLog BUGS AUTHORS TODO DOCUMENTATION
%attr(755,root,root) %{_bindir}/gtkhx
%dir %{_datadir}/gtkhx
%{_datadir}/gtkhx/icons.rsrc
%dir %{_datadir}/gtkhx/sounds
%{_datadir}/gtkhx/sounds/chatinvite.aiff
%{_datadir}/gtkhx/sounds/chatpost.aiff
%{_datadir}/gtkhx/sounds/error.aiff
%{_datadir}/gtkhx/sounds/filedone.aiff
%{_datadir}/gtkhx/sounds/join.aiff
%{_datadir}/gtkhx/sounds/logged-in.aiff
%{_datadir}/gtkhx/sounds/message.aiff
%{_datadir}/gtkhx/sounds/newspost.aiff
%{_datadir}/gtkhx/sounds/part.aiff
#%{_datadir}/gtkhx/gtkhx_pixmap.png
%{_mandir}/man1/*
